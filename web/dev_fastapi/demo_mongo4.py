# https://www.mongodb.com/developer/quickstart/python-quickstart-fastapi/
# mongo + fastapi

# from black import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from pydantic import BaseModel, Field
from fastapi import FastAPI, Body, HTTPException
from typing import Optional, List

# conn = AsyncIOMotorClient('localhost', 27017)
client = AsyncIOMotorClient('mongodb://root:123456@127.0.0.1:27017/sft')
db = client['sft']


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class User(BaseModel):
    username: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "username": "zhangsan"
            }
        }

# 很粗糙的处理，不Pythonic
class IUser(User):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    username: str = Field(...)
    password: Optional[str] = None

    class Config:
        allow_population_by_field_name = True   # https://www.5axxw.com/questions/content/oveaou
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "username": "zhangsan",
                "password": "123456",
            }
        }


app = FastAPI()

@app.post('/', response_model=IUser)
async def create_user(user: IUser = Body(...)):
    print('-------', user)
    insert_result = await db["users"].insert_one(user.dict())
    print('+++', insert_result.inserted_id)
    created_user = await db["users"].find_one({"_id": insert_result.inserted_id})
    print('###', created_user)
    return created_user


@app.get('/', response_model=IUser)
async def get_user(query: User = Body(...)):
    print('-------', query)
    if (user := await db["users"].find_one(query.dict())) is not None:
        return user
    raise HTTPException(status_code=404, detail=f"User {id} not found")


@app.get('/list', response_model=List[IUser])
async def list_user():
    users = await db["users"].find().to_list(10)
    return users


@app.put('/update/{username}', response_model=IUser)
async def update_user(username:str, query: User = Body(...)):
    print('-------', query)
    query = {k: v for k, v in query.dict().items() if v is not None}
    print('--', query)

    if len(query) >= 1:
        update_result = await db['users'].update_one({'username': username}, {'$set': query})
        if update_result.modified_count == 1:
            if (existing_user := await db["users"].find_one(query)) is not None:
                return existing_user
    raise HTTPException(status_code=404, detail=f"User {id} not found")



@app.delete('/')
async def delete_user(query: User = Body(...)):
    print('-------', query)
    # delete_result = await db["users"].delete_one(query.dict())
    delete_result = await db["users"].delete_many(query.dict())
    if delete_result.deleted_count >= 1:
        return {'delete': 'ok'}
    return {'delete': 'not found user'}

# uvicorn demo_mongo4:app --reload
# 这个例子比较特别，在get请求中包含body。（一般不这样做，但也可以）
# curl -X 'POST'   'http://127.0.0.1:8001/'   -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{  "username": "zhangsan",  "password": "123456"}'
# curl -X 'GET' 'http://127.0.0.1:8001/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"username": "zhangsan"}'

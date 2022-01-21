from pydantic import BaseModel, Field
from fastapi.encoders import jsonable_encoder
from bson import ObjectId   # mongodb id


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
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    username: str = Field(...)
    password: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        # json_encoders = {ObjectId: objectid2int}  # 使用自定义的类型转换
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "username": "zhangsan",
                "password": "123456",
            }
        }


class UserOut(User):
    id: str = Field(None)


print(User.schema(by_alias=True))
print(UserOut.schema(by_alias=True))
print('---')

user1 = User(_id=ObjectId(), username='zhangsan', password='123456')
print(user1.dict()) # dict与jsonable_encoder解析pydantic模型的方式不一样
print(jsonable_encoder(user1))
print(jsonable_encoder(user1, by_alias=False))  # 不使用别名作为key
print('---')

# user_out1 = UserOut(**jsonable_encoder(user1, by_alias=False))
# print(jsonable_encoder(user_out1))

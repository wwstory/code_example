from fastapi import APIRouter, HTTPException, Depends, Path, File, UploadFile
from typing import List

from ..model.schemas.user import User
from ..utils.database import GetIncCounterId
from ..utils.minio import upload_object, get_object_json

router = APIRouter(tags=['用户管理'])


fake_db = [
    {'username': 'zhangsan', 'password': '123456'},
    {'username': 'luo', 'password': '123'},
]


@router.post('/user', response_model=User)
async def create_user(user: User, id: int = Depends(GetIncCounterId('test').get_id)):
    print('#', id)
    fake_db.append(user.dict())
    return user


@router.get('/user/{id}', response_model=User)
async def get_user(id: int):
    if id == 4:
        raise HTTPException(status_code=418, detail="Nope! I don't like 4.")
    user = User(**fake_db[id])
    return user


@router.get('/users', response_model=List[User])
async def get_users():
    user = fake_db
    return user


@router.post('/file')
async def upload_file(file: UploadFile = File(...),):
    file_name = await upload_object(file)
    return {'file_name': file_name}


@router.get('/file/{file_name}')
async def get_file(file_name: str = Path(...)):
    response = await get_object_json(file_name)
    return response

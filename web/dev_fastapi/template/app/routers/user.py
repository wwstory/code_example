from fastapi import APIRouter, HTTPException, Depends
from typing import List

from ..model.schemas.user import User
from ..utils.database import GetCounterId

router = APIRouter(tags=['用户管理'])


fake_db = [
    {'username': 'zhangsan', 'password': '123456'},
    {'username': 'luo', 'password': '123'},
]


@router.post('/user', response_model=User)
async def create_user(user: User, id: int = Depends(GetCounterId('test').get_id)):
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

# 异步router api的测试： https://fastapi.tiangolo.com/advanced/async-tests/

import pytest
from httpx import AsyncClient

from app.main import app


# @pytest.mark.anyio    # depends trio, it cause twice call (数据插入将会执行2次)
@pytest.mark.asyncio
async def test_post_user():
    # async with AsyncClient(app=app, base_url='http://127.0.0.1:8000') as ac:  # 由于router中带有await,会报错,原因暂未明确
    async with AsyncClient(base_url='http://127.0.0.1:8000') as ac: # 不传递`app=app`, 测试需要先手动启动项目
        response = await ac.post('/api/user', json={'username': 'wwstory', 'password': '7654321'})
    assert response.status_code == 200
    assert response.json() == {
        'username': 'wwstory',
        'password': '7654321'
    }


@pytest.mark.asyncio
async def test_get_user():
    async with AsyncClient(app=app, base_url='http://127.0.0.1:8000') as ac:
        response = await ac.get('/api/user/0')
    assert response.status_code == 200
    assert response.json() == {
        'username': 'zhangsan',
        'password': '123456'
    }

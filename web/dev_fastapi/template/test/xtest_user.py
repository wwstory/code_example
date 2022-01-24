# 同步router api的测试
# 文件前缀不以test_命名，将不会得到测试

from http import client
from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_post_user():
    response = client.post(
        '/api/user',
        headers={'X-Token': 'wxyz'},
        json={'username': 'wwstory', 'password': '7654321'}
    )
    assert response.status_code == 200
    assert response.json() == {
        'username': 'wwstory',
        'password': '7654321'
    }


def test_get_user():
    response = client.get('/api/user/0')
    assert response.status_code == 200
    assert response.json() == {
        'username': 'zhangsan',
        'password': '123456'
    }

# https://www.cnblogs.com/aduner/p/13532504.html
# 官网文档： https://motor.readthedocs.io/en/stable/api-asyncio/cursors.html
# 异步调用（pymongo是同步操作）

from black import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

# conn = AsyncIOMotorClient('localhost', 27017)
client = AsyncIOMotorClient('mongodb://root:123456@127.0.0.1:27017/sft')
db = client['sft']
coll = db["users"]

async def do_insert():
    # # 增
    print('\n\n---增')
    await coll.insert_one({"username": "wangwu", "password": "654321", "age": 18})
    await coll.insert_many([{"username": "test1", "password": "test1"}, {"username": "test1", "password": "test2", "email": "test1@qq.com"}, {"username": "test2", "password": "test2"}])
    print('增---')

async def do_find():
    # 查
    print('\n\n---查')
    r = await coll.find_one({"username": "wangwu"})
    print(r)
    # async for r in coll.find({"username": "test1"}):
    #     print(r)
    # print([r async for r in coll.find({"username": "test1"})])
    # r = await coll.find({"username": "test1"}).to_list(length=None)
    r = await coll.find({"username": "test1"}).to_list(length=10)
    print(r)
    print('查---')

async def do_update():
    # 改
    print('\n\n---改')
    await coll.update_one({"username": "wangwu"}, {"$set": {"password": "1234567"}})
    r = await coll.find_one({"username": "wangwu"})
    print(r)
    print('改---')

async def do_delete():
    # 删
    print('\n\n---删')
    await coll.delete_one({"username": "wangwu"})
    await coll.delete_many({"username": "test1"})
    await coll.delete_many({"username": "test2"})
    print('删---')

asyncio.get_event_loop().run_until_complete(do_insert())
asyncio.get_event_loop().run_until_complete(do_find())
asyncio.get_event_loop().run_until_complete(do_update())
asyncio.get_event_loop().run_until_complete(do_delete())

# %%

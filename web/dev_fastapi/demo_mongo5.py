# 简单的关联，包含聚合操作表: https://www.cnblogs.com/xuliuzai/p/10055535.html
# 关联多个集合: https://www.5axxw.com/questions/content/cip9aj
# aggregate不能使用await: https://motor.readthedocs.io/en/stable/api-asyncio/asyncio_motor_database.html?highlight=aggregate#motor.motor_asyncio.AsyncIOMotorDatabase.aggregate
# 2个集合关联查询

from black import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

# conn = AsyncIOMotorClient('localhost', 27017)
client = AsyncIOMotorClient('mongodb://root:123456@127.0.0.1:27017/sft')
db = client['sft']

async def do_insert():
    # 增
    print('\n\n---增')
    await db["users"].insert_one({"username": "wangwu", "password": "654321"})
    await db["lv"].insert_one({"username2": "wangwu", 'age': 18})
    print('增---')

async def do_find():
    # 查
    print('\n\n---查')
    # pipeline = [{
    #     '$lookup':{
    #         'from': 'lv',
    #         'localField': 'username',
    #         'foreignField': 'username2',
    #         'as': 'lv'
    #     }
    # }]  # motor中不支持单个{}，必须是list
    pipeline = [
        {
            '$match':
            {
                'username': 'wangwu'
            }
        },
        {
            '$lookup':
            {
                'from': 'lv',
                'localField': 'username',
                'foreignField': 'username2',
                'as': 'lv'
            }
        },
        {
            '$set':
            {
                'lv':
                {
                    '$arrayElemAt': # 选择第几个元素（去括号[]）
                    [
                        '$lv',
                        0
                    ]
                }
            }
        },
        {
            '$project': # 选择输出的字段
            {
                # '_id': 1, # 1或True是一样的含义
                '_id': True,
                'username': True,
                'password': True,
                'lv': '$lv.age'
            }
        }
    ]  # motor中不支持单个{}，必须是list
    # async for r in db["users"].aggregate(pipeline):
    #     print(r)
    r = await db["users"].aggregate(pipeline).to_list(10)
    print(r)
    print('查---')

async def do_delete():
    # 删
    print('\n\n---删')
    await db["users"].delete_many({"username": "wangwu"})
    await db["lv"].delete_many({"username2": "wangwu"})
    print('删---')

asyncio.get_event_loop().run_until_complete(do_insert())
asyncio.get_event_loop().run_until_complete(do_find())
asyncio.get_event_loop().run_until_complete(do_delete())

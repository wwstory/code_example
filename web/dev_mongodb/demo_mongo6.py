# https://motor.readthedocs.io/en/stable/api-tornado/motor_collection.html#motor.motor_tornado.MotorCollection.find_one_and_update
# 获取递增id

from black import asyncio
from motor.motor_asyncio import AsyncIOMotorClient


client = AsyncIOMotorClient('mongodb://root:123456@127.0.0.1:27017/sft')
db = client['sft']


# mongo cmd: db.incre_system.findAndModify({query:{'table':'test'}, update:{$inc:{'id':1}}, new:true, upsert:true})
async def get_mongo_counter(db, collection_name='') -> int:
    id = await db['counter_id'].find_one_and_update(
        {'collection': collection_name},    # 查询
        {'$inc': {'id': 1}},                # 递增字段
        upsert=True,                        # 如果不存在，将新建
        projection={'id': True, '_id': False},  # 返回的字段
        return_document=True,               # 返回递增前(False)，还是递增后(True)的结果
    )
    return id


print(asyncio.get_event_loop().run_until_complete(get_mongo_counter(db, 'test')))
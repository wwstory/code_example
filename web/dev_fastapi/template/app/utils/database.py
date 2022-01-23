from motor.motor_asyncio import AsyncIOMotorClient

from ..config import conf


client = AsyncIOMotorClient(f'mongodb://{conf.mongodb.username}:{conf.mongodb.password}@{conf.mongodb.ip}:{conf.mongodb.port}/{conf.mongodb.database}')
database = client[conf.mongodb.database]


def get_db():
    db = database
    try:
        yield db
    finally:
        pass


async def get_collection_counter_id(db, collection_name='test') -> int:
    result = await db['counter_id'].find_one_and_update(
        {'collection': collection_name},    # 查询
        {'$inc': {'id': 1}},                # 递增字段
        upsert=True,                        # 如果不存在，将新建
        projection={'id': True, '_id': False},  # 返回的字段
        return_document=True,               # 返回递增前(False)，还是递增后(True)的结果
    )
    return result.get('id')

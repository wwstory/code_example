from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from ..config import conf


client = AsyncIOMotorClient(f'mongodb://{conf.mongo.username}:{conf.mongo.password}@{conf.mongo.ip}:{conf.mongo.port}/{conf.mongo.database}')
db = client[conf.mongo.database]


def get_db():
    global db
    try:
        yield db
    finally:
        pass


async def get_and_inc_collection_counter_id(collection_name='test') -> int:
    result = await db['counter_id'].find_one_and_update(
        {'collection': collection_name},    # 查询
        {'$inc': {'id': 1}},                # 递增字段
        upsert=True,                        # 如果不存在，将新建
        projection={'id': True, '_id': False},  # 返回的字段
        return_document=True,               # 返回递增前(False)，还是递增后(True)的结果
    )
    return result.get('id')


class GetIncCounterId:
    '''
    使用类包装get_collection_counter_id方法
    '''
    def __init__(self, collection_name='test'):
        global db
        self.db = db
        self.collection_name = collection_name
    
    async def get_id(self):
        result = await self.db['counter_id'].find_one_and_update(
            {'collection': self.collection_name},
            {'$inc': {'id': 1}},
            upsert=True,
            projection={'id': True, '_id': False},
            return_document=True,
        )
        return result.get('id')


async def get_collection_counter_id(collection_name='test') -> int:
    result = await db['counter_id'].find_one(
        {'collection': collection_name},    # 查询
        projection={'id': True, '_id': False},  # 返回的字段
    )
    return result.get('id')


# https://www.mongodb.com/developer/quickstart/python-quickstart-fastapi/
# mongo + fastapi

from black import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

# conn = AsyncIOMotorClient('localhost', 27017)
client = AsyncIOMotorClient('mongodb://root:123456@127.0.0.1:27017/sft')
db = client['sft']
coll = db["users"]

async def do_find():
    # 查
    print('\n\n---查')
    r = await coll.find_one()
    print(r)
    print('查---')

print('---')
asyncio.get_event_loop().run_until_complete(do_find())
print('---')
client.close()
# db.close() # error
asyncio.get_event_loop().run_until_complete(do_find())

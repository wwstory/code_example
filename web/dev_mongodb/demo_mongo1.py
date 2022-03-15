# https://kb.objectrocket.com/mongo-db/how-to-query-mongodb-documents-in-python-269

from pymongo import MongoClient

# client = MongoClient('mongodb://root:123456@127.0.0.1:27017/sft')
client = MongoClient(
    '127.0.0.1',
    27017,
)
db = client['sft']
db.authenticate("root", "123456")
print(db.list_collection_names())
print(list(db.users.find()))
coll = db["users"]
# # 增
print('\n\n---增')
print(coll.insert_one({"username": "wangwu", "password": "654321", "age": 18}))
print(coll.insert_many([{"username": "test1", "password": "test1"}, {"username": "test1", "password": "test2", "email": "test1@qq.com"}, {"username": "test2", "password": "test2"}]))
# 查
print('\n\n---查')
print(coll.find_one())
print(coll.find_one({"username": "wangwu"}))
print(list(coll.find({"username": "test1"})))
print(list(coll.find({"username": {"$regex": "^test"}})))   # 正则：以test开头的
print(list(coll.find({"$or": [{"username": "test1"}, {"username": "test2"}]})))   # or
print(list(coll.find({"age": {"$gte": 18}})))   # 大于
# 改
print('\n\n---改')
print(coll.update_one({"username": "test1", "password": "test2"}, {"$set": {"username": "test1", "password": "test3"}}))
print(coll.find_one({"username": "test1", "password": "test3"}))
# 删
print('\n\n---删')
coll.delete_one({"username": "wangwu"})
coll.delete_many({"username": "test1"})
coll.delete_many({"username": "test2"})


import pymongo
from pymongo import MongoClient, IndexModel
from pymongo.database import Database
from pprint import pprint


# mongodb: https://docs.mongodb.com/manual/core/index-unique/


client = MongoClient(f'mongodb://root:123456@127.0.0.1:27017/sft')
db = client['sft']

# 1.当username和password都一样，才报错。
# https://api.mongodb.com/python/3.2/api/pymongo/collection.html?highlight=create_indexes#pymongo.collection.Collection.create_index
db['user'].create_index([('username', pymongo.ASCENDING), ('password', pymongo.ASCENDING)], unique=True)

# 2
# 拆分执行，username或password有一个字段一样，则报错
db['user'].create_index([('username', pymongo.ASCENDING)], unique=True)
db['user'].create_index([('password', pymongo.ASCENDING)], unique=True)
# 与上述等价
# https://api.mongodb.com/python/3.2/api/pymongo/collection.html?highlight=create_indexes#pymongo.collection.Collection.create_indexes
db['user'].create_indexes([IndexModel([('username', pymongo.ASCENDING)], unique=True), IndexModel([('password', pymongo.ASCENDING)], unique=True)])


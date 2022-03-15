import casbin
import casbin_pymongo_adapter


# adapter = casbin_pymongo_adapter.Adapter('mongodb://root:123456@127.0.0.1:27017/', "test_db")   # error, because default database is admin
adapter = casbin_pymongo_adapter.Adapter('mongodb://root:123456@127.0.0.1:27017/test_db', "test_db")


# e = casbin.Enforcer('./model.conf', './policy.csv')
e = casbin.Enforcer('./model.conf', adapter)

r = e.add_policy("zhangsan", "data1", "read")
print('===== add success?', r)


# sub = "alice"  # 想要访问资源的用户
# obj = "data1"  # 将要被访问的资源
# act = "read"  # 用户对资源进行的操作

for sub, obj, act in [
    ("alice", "data1", "read"),
    ("zhangsan", "data1", "read"),
]:
    if e.enforce(sub, obj, act):
        # 允许alice读取data1
        print('pass')
    else:
        # 拒绝请求，抛出异常
        print('fail')


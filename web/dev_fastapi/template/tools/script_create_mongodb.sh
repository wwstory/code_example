#/bin/sh

USER_NAME=root
USER_PASSWORD=123456
MONGO_INITDB_ROOT_USERNAME=admin
MONGO_INITDB_ROOT_PASSWORD=admin


# # docker exec -it mongo bash
# docker exec -i mongo bash <<EOF
# mongo
# use admin
# db.createUser({user: "${MONGO_INITDB_ROOT_USERNAME}", pwd: "${MONGO_INITDB_ROOT_PASSWORD}", customData:{name:"zhangsan", email:"xxx@qq.com"}, roles: [{role: "userAdminAnyDatabase", db:"admin"}]});
# db.auth("${MONGO_INITDB_ROOT_USERNAME}", "${MONGO_INITDB_ROOT_PASSWORD}");
# use sft
# db.createUser({user: "${USER_NAME}", pwd: "${USER_PASSWORD}", roles: [{role: "readWrite", db:"sft"}]});
# show users;
# db.system.users.find().pretty();
# exit
# EOF

docker run -d --name mongo -p 27017:27017 \
    -e MONGO_INITDB_ROOT_USERNAME=${MONGO_INITDB_ROOT_USERNAME} \
    -e MONGO_INITDB_ROOT_PASSWORD=${MONGO_INITDB_ROOT_PASSWORD} \
    mongo --auth

# 新增-e后，延时从2s->3s才能完成
sleep 3

docker exec -i mongo bash <<EOF
mongo
use admin
db.auth("${MONGO_INITDB_ROOT_USERNAME}", "${MONGO_INITDB_ROOT_PASSWORD}");
use sft
db.createUser({user: "${USER_NAME}", pwd: "${USER_PASSWORD}", roles: [{role: "readWrite", db:"sft"}]});
exit
EOF

insert_data(){
docker exec -i mongo bash <<EOF
mongo sft
db.auth("${USER_NAME}", "${USER_PASSWORD}");

db.createCollection("users")
db.users.insert({username: "", password: "", email: "", nickname: "", avatar: "", deleted_at: new Date(), created_at: new Date(), updated_at: new Date()})
db.users.insert({username: "zhangsan", password: "123456", email: "zhangsan@qq.com", nickname: "", avatar: "", deleted_at: new Date(), created_at: new Date(), updated_at: new Date()})
db.users.insert({username: "lisi", password: "12345", email: "lisi@qq.com", nickname: "", avatar: "", deleted_at: new Date(), created_at: new Date(), updated_at: new Date()})

exit
EOF
}

if [ ${1} ] && [ ${1} = insert_data ];then
    insert_data
fi

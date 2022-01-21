#/bin/sh

USER_NAME=root
USER_PASSWORD=123456
USER_ADMIN_NAME=admin
USER_ADMIN_PASSWORD=admin

# docker stop mongo; docker rm mongo
docker run -d --name mongo -p 27017:27017 mongo --auth

sleep 2
# docker exec -i mongo bash <<EOF
# mongo
# use admin
# db.createUser({user: "admin", pwd: "admin", customData:{name:"zhangsan", email:"xxx@qq.com"} roles: [{role: "userAdminAnyDatabase", db:"admin"}]});
# db.auth("admin", "admin");
# show users;
# db.system.users.find().pretty();
# use sft
# db.createUser({user: "root", pwd: "root", roles: [{role: "readWrite", db:"sft"}]});
# db.auth("root", "root");
# exit
# EOF

docker exec -i mongo bash <<EOF
mongo
use admin
db.createUser({user: "${USER_ADMIN_NAME}", pwd: "${USER_ADMIN_PASSWORD}", roles: [{role: "userAdminAnyDatabase", db:"admin"}]});
db.auth("${USER_ADMIN_NAME}", "${USER_ADMIN_PASSWORD}");
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


db.createCollection("scenarios")


db.createCollection("plan_collections")


db.createCollection("plans_targets")


db.createCollection("opponents")


db.createCollection("entity_categories")


db.createCollection("task_categories")


db.createCollection("cognition_systems")


db.createCollection("state_dictionaries")


db.createCollection("plans_tasks")

db.createCollection("plans_task_details")


exit
EOF
}

if [ ${1} ] && [ ${1} = insert_data ];then
    insert_data
fi

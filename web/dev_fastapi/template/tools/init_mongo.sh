#/bin/sh

# 没有用到，在docker-compose.yml中，如果mongo没有映射/docker-entrypoint-initdb.d初始化，将需要进入容器，手动执行以下命令创建用户

MONGO_USER_NAME=${MONGO_USER_NAME:-root}
MONGO_USER_PASSWORD=${MONGO_USER_PASSWORD:-123456}
MONGO_DATABASE={MONGO_DATABASE:-sft}

mongo <<EOF
use admin
db.auth("${MONGO_INITDB_ROOT_USERNAME}", "${MONGO_INITDB_ROOT_PASSWORD}");
use ${MONGO_DATABASE}
db.createUser({user: "${MONGO_USER_NAME}", pwd: "${MONGO_USER_PASSWORD}", roles: [{role: "readWrite", db:"${MONGO_DATABASE}"}]});
exit
EOF

#!/bin/bash

# 所有run.sh的环境变量，都需要在docker-compose中的services.demo-server.environment再配置一遍。是为了server所处的容器，添加这些环境变量，然后在app/config/conf.yaml中解析。

# server
export SERVER_IP=192.168.2.13
# mongo
export MONGO_INITDB_ROOT_USERNAME=admin
export MONGO_INITDB_ROOT_PASSWORD=admin
export MONGO_USER_NAME=root         # docker-compose.yml mongo.environment # 为了tools/init_mongo.sh，当mongo容器启动时，脚本将会被映射，执行。此时所处容器，得不到在此处设置的环境变量
export MONGO_USER_PASSWORD=123456   # docker-compose.yml mongo.environment
export MONGO_DATABASE=sft           # docker-compose.yml mongo.environment
export MONGO_SERVER_IP=${SERVER_IP}
# minio
export MINIO_ACCESS_KEY=minioadmin
export MINIO_SECRET_KEY=minioadmin
export MINIO_SERVER_IP=${SERVER_IP}
export MINIO_BUCKET_NAME=sft

pytest
uvicorn app.main:app --reload

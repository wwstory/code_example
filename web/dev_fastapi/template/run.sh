#!/bin/bash

# 所有run.sh的环境变量，都需要在docker-compose中的services.sft-server.environment再配置一遍

# server
export SERVER_IP=192.168.2.13
# mongo
export MONGO_INITDB_ROOT_USERNAME=admin
export MONGO_INITDB_ROOT_PASSWORD=admin
export MONGO_USER_NAME=root
export MONGO_USER_PASSWORD=123456
export MONGO_DATABASE=sft
export MONGO_SERVER_IP=${SERVER_IP}
# minio
export MINIO_ACCESS_KEY=minioadmin
export MINIO_SECRET_KEY=minioadmin
export MINIO_SERVER_IP=${SERVER_IP}

docker-compose up

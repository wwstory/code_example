#/bin/sh

ACCESS_KEY=minioadmin
SECRET_KEY=minioadmin
LOAL_PATH=/tmp/data
BUCKET_NAME=sft
SERVER_NAME=my_minio
SERVER_URL=http://172.17.0.2:9000

docker run -d \
    -p 9000:9000 \
    -e "MINIO_ACCESS_KEY=${ACCESS_KEY}" \
    -e "MINIO_SECRET_KEY=${SECRET_KEY}" \
    -v ${LOAL_PATH}:/data \
    minio/minio server /data

sleep 2

# http://docs.minio.org.cn/docs/master/minio-client-complete-guide
# docker run --rm minio/mc ls play
# docker run --rm -it --entrypoint=/bin/sh minio/mc << EOF
docker run --rm -i --entrypoint=/bin/sh minio/mc << EOF
mc config host add ${SERVER_NAME} ${SERVER_URL} ${ACCESS_KEY} ${SECRET_KEY}
mc mb ${SERVER_NAME}/${BUCKET_NAME}
mc policy set public ${SERVER_NAME}/${BUCKET_NAME}
exit
EOF

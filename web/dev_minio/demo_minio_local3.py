# 引入MinIO包。
from minio import Minio
from minio.error import InvalidResponseError
from datetime import timedelta

# 使用endpoint、access key和secret key来初始化minioClient对象。
minioClient = Minio('172.17.0.2:9000',
                    access_key='minioadmin',
                    secret_key='minioadmin',
                    secure=False)

# presigned get object URL for object name, expires in 2 days.
try:
    print(minioClient.presigned_get_object('wwbucket', 'serah.jpg', expires=timedelta(days=2)))
# Response error is still possible since internally presigned does get bucket location.
except InvalidResponseError as err:
    print(err)
# 引入MinIO包。
from minio import Minio
from minio.error import InvalidResponseError

# 使用endpoint、access key和secret key来初始化minioClient对象。
minioClient = Minio('172.17.0.2:9000',
                    access_key='minioadmin',
                    secret_key='minioadmin',
                    secure=False)


# Get a full object and prints the original object stat information.
try:
    print(minioClient.fget_object('wwbucket', 'serah.jpg', './download_serah.jpg'))
except InvalidResponseError as err:
    print(err)
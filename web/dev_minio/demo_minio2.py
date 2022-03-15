# 引入MinIO包。
from minio import Minio
from minio.error import MinioException, ServerError

# 使用endpoint、access key和secret key来初始化minioClient对象。
minioClient = Minio('play.min.io',
                    access_key='Q3AM3UQ867SPQQA43P2F',
                    secret_key='zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG',
                    secure=True)


# Get a full object and prints the original object stat information.
try:
    print(minioClient.fget_object('wwbucket', 'serah.jpg', './download_serah.jpg'))
except MinioException as err:
    print(err)
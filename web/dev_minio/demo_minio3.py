# 引入MinIO包。
from minio import Minio
from minio.error import MinioException, ServerError
from datetime import timedelta

# 使用endpoint、access key和secret key来初始化minioClient对象。
minioClient = Minio('play.min.io',
                    access_key='Q3AM3UQ867SPQQA43P2F',
                    secret_key='zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG',
                    secure=True)

# presigned get object URL for object name, expires in 2 days.
try:
    print(minioClient.presigned_get_object('wwbucket', 'serah.jpg', expires=timedelta(days=2)))
# Response error is still possible since internally presigned does get bucket location.
except MinioException as err:
    print(err)
# 引入MinIO包。
from minio import Minio
from minio.error import MinioException, ServerError

# 使用endpoint、access key和secret key来初始化minioClient对象。
minioClient = Minio('play.min.io',
                    access_key='Q3AM3UQ867SPQQA43P2F',
                    secret_key='zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG',
                    secure=True)    # https://docs.min.io/docs/how-to-secure-access-to-minio-server-with-tls.html

# 调用make_bucket来创建一个存储桶。
try:
    if not minioClient.bucket_exists('wwbucket'):
        minioClient.make_bucket("wwbucket", location="us-east-1")
except MinioException as err:
    pass
else:
    try:
        # minioClient.fput_object('wwbucket', '/dir/serah.jpg', './serah.jpg')
        # minioClient.fput_object('wwbucket', 'dir/serah.jpg', './serah.jpg')
        minioClient.fput_object('wwbucket', 'serah.jpg', './serah.jpg')
    except MinioException as err:
        print(err)

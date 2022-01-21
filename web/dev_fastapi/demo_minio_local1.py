# 引入MinIO包。
from minio import Minio
from minio.error import MinioException, InvalidResponseError

# 使用endpoint、access key和secret key来初始化minioClient对象。
minioClient = Minio('172.17.0.2:9000',
                    access_key='minioadmin',
                    secret_key='minioadmin',
                    secure=False)   # https://docs.min.io/docs/how-to-secure-access-to-minio-server-with-tls.html

# 调用make_bucket来创建一个存储桶。
try:
    if not minioClient.bucket_exists('wwbucket'):
        minioClient.make_bucket("wwbucket")
except MinioException as err:
    pass
else:
    try:
        # minioClient.fput_object('wwbucket', '/dir/tmp.log', './tmp.log')
        minioClient.fput_object('wwbucket', 'serah.jpg', './serah.jpg')
    except InvalidResponseError as err:
        print(err)

# https://gitanswer.com/fastapi-question-how-can-i-receive-uploadfile-and-send-to-minio-server-without-write-to-temp-folder-python-493622883
from minio import Minio
from minio.error import InvalidResponseError
import os


minioClient = Minio('play.min.io',
                    access_key='Q3AM3UQ867SPQQA43P2F',
                    secret_key='zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG',
                    secure=True)

try:
    with open('./serah.jpg', 'rb') as f:
        file_size = os.fstat(f.fileno()).st_size    # 从打开的文件对象中，读取文件描述符，读取文件大小
        minioClient.put_object('wwbucket', 'serah.jpg', f, file_size)
except InvalidResponseError as err:
    print(err)
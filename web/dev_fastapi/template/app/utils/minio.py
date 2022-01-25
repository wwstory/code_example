from minio import Minio
from minio.error import InvalidResponseError
from fastapi import UploadFile
from fastapi.responses import StreamingResponse
import os
from datetime import timedelta
from uuid import uuid4
import json

from ..config import conf


minioClient = Minio(f'{conf.minio.ip}:{conf.minio.port}',
                    access_key=conf.minio.access_key,
                    secret_key=conf.minio.secret_key,
                    secure=conf.minio.secure)


try:
    if not minioClient.bucket_exists(conf.minio.bucket):
        minioClient.make_bucket(conf.minio.bucket)
except InvalidResponseError as e:
    print('无法创建Bucket!')
    raise e
# try:
#     minioClient.set_bucket_policy(conf.minio.bucket, json.dumps({}))  # https://docs.min.io/docs/python-client-api-reference.html#set_bucket_policy
# except InvalidResponseError as e:
#     raise


def upload_object(file: UploadFile, prefix='', bucket_name=conf.minio.bucket, use_uuid=True) -> str:
    global minioClient
    try:
        file_size = os.fstat(file.file.fileno()).st_size
        file_name = f'{uuid4()}{os.path.splitext(file.filename)[1]}' if use_uuid else file.filename
        file_name = os.path.join(prefix, file_name)
        minioClient.put_object(bucket_name, file_name, file.file, file_size)
        return file_name
    except InvalidResponseError as e:
        raise e


def get_object_content(object_name, bucket_name=conf.minio.bucket):
    global minioClient
    try:
        data = minioClient.get_object(bucket_name, object_name)
        return StreamingResponse(data.stream())
    except InvalidResponseError as e:
        raise e


def get_object_json(object_name, bucket_name=conf.minio.bucket):
    global minioClient
    try:
        data = minioClient.get_object(bucket_name, object_name)
        return json.loads(data.data)
    except InvalidResponseError as e:
        raise e


def get_object_url(object_name, bucket_name=conf.minio.bucket, use_presigned=False, expires=timedelta(days=7)) -> str:
    if use_presigned:
        file_url = f'{conf.minio.ip}:{conf.minio.port}/{bucket_name}/{object_name}'
    else:
        try:
            global minioClient
            file_url = minioClient.presigned_get_object(bucket_name, object_name, expires=expires)
        except InvalidResponseError as e:
            raise e
    return file_url

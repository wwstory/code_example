from minio import Minio
from minio.error import InvalidResponseError
from fastapi import UploadFile
from fastapi.responses import StreamingResponse
import os
from datetime import timedelta
from uuid import uuid4

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


async def upload_object(file: UploadFile, prefix='', bucket_name=conf.minio.bucket, use_uuid=True, use_presigned=False, expires=timedelta(days=7)) -> str:
    try:
        file_size = os.fstat(file.file.fileno()).st_size
        file_name = f'{uuid4()}{os.path.splitext(file.filename)[1]}' if use_uuid else file.filename
        file_name = os.path.join(prefix, file_name)
        minioClient.put_object(bucket_name, file_name, file.file, file_size)
        return file_name
    except InvalidResponseError as e:
        raise e


async def get_object_content(object_name, bucket_name=conf.minio.bucket):
    try:
        data = minioClient.fget_object(bucket_name, object_name)
        return StreamingResponse(data.stream())
    except InvalidResponseError as e:
        raise e


async def get_object_json(object_name, bucket_name=conf.minio.bucket):
    return get_object_content(object_name, bucket_name=bucket_name)


async def get_object_url(object_name, bucket_name=conf.minio.bucket, use_presigned=False, expires=timedelta(days=7)) -> str:
    if use_presigned:
        file_url = f'{conf.minio.ip}:{conf.minio.port}/{bucket_name}/{object_name}'
    else:
        try:
            file_url = minioClient.presigned_get_object(bucket_name, object_name, expires=expires)
        except InvalidResponseError as e:
            raise e
    return file_url

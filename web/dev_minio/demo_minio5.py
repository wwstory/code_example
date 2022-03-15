# 引入MinIO包。
from minio import Minio
from minio.error import InvalidResponseError
from fastapi import FastAPI
from fastapi.responses import StreamingResponse, FileResponse
import json


app = FastAPI()

# 使用endpoint、access key和secret key来初始化minioClient对象。
minioClient = Minio('play.min.io',
                    access_key='Q3AM3UQ867SPQQA43P2F',
                    secret_key='zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG',
                    secure=True)


@app.get('/')
async def get_content():
    try:
        obj = minioClient.get_object('wwbucket', 'tmp.json')
    except InvalidResponseError as err:
        print(err)
    # 以下四种方式都可以实现：
    # return json.loads(obj.data.decode())
    # return json.loads(obj.data)               # json直接解析二进制数据, 不会解析unicode编码
    return StreamingResponse(obj.stream())
    # return FileResponse('./tmp.json')        # 从本地文件返回
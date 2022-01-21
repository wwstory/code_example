# https://fastapi.tiangolo.com/zh/tutorial/middleware/

import time

from fastapi import FastAPI, Request

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'hello world'}

@app.middleware("http") # 当前只支持"http"
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    print('cost time:', process_time)
    return response

@app.middleware("http")
async def test(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time2"] = str(process_time)
    print('cost time2:', process_time)
    return response

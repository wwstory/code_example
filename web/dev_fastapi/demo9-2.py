# https://stackoverflow.com/questions/60778279/fastapi-middleware-peeking-into-responses
# https://fastapi.tiangolo.com/zh/tutorial/middleware/

from fastapi import FastAPI, Request, Response


app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'hello world'}


@app.middleware("http") # 当前只支持"http"
async def deal_body(request: Request, call_next):
    response = await call_next(request)
    body = b''
    async for chunk in response.body_iterator:  # 访问生成器消耗了数据
        body += chunk
        print(body)
    # do something with body ...
    return Response(
        content=body,
        status_code=response.status_code,
        headers=dict(response.headers),
        media_type=response.media_type
    )

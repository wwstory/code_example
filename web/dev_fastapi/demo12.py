# https://fastapi.tiangolo.com/zh/tutorial/handling-errors/
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.post("/")
async def create_item(item: Item):
    return item


fake_db = [
    {'name': 'zhangsan', 'price': 12},
    {'name': 'lisi', 'price': 15, 'tax': 0.2},
    {'name': 'wangwu', 'price': 11, 'description': 'hello world!', 'tax': 0.1},
]

@app.get("/{id}")
async def get_item(id: int):
    if id > 2:      # 如果路径查询参数大于2，将抛出错误
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")    # 如果没有定义：my_http_exception_handler，将返回detail中的数据
    item = Item(**fake_db[id])
    return item




from fastapi import Request, status
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import RequestValidationError, HTTPException

@app.exception_handler(RequestValidationError)
async def my_request_validation_exception_handler(request: Request, exc: RequestValidationError):   # 数据验证时
    print('---------------xxxxxxxxx--------------------')
    # return PlainTextResponse('hello', status_code=exc.status_code)    # 返回朴素字符串
    return JSONResponse(
        status_code=400,
        # content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
        content={"status": 1001, "message": 'hi error!'},
    )

@app.exception_handler(HTTPException)
async def my_http_exception_handler(request: Request, exc: HTTPException):  # 请求无效数据时
    print('---------------yyyyyyyyyy--------------------')
    return JSONResponse(
        status_code=exc.status_code,
        # content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
        content={"status": 1002, "message": 'ni hao error!'},
    )
from fastapi import FastAPI
from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError, HTTPException


def load_exception_handler(app: FastAPI):
    @app.exception_handler(RequestValidationError)
    async def my_request_validation_exception_handler(request: Request, e: RequestValidationError):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={'status': status.HTTP_400_BAD_REQUEST, 'msg': '无效的参数'},
        )


    @app.exception_handler(HTTPException)
    async def my_http_exception_handler(request: Request, e: HTTPException):
        return JSONResponse(
            status_code=e.status_code,
            content={'status': e.status_code, 'msg': e.detail},
        )

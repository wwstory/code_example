# https://fastapi.tiangolo.com/zh/tutorial/cors/
# https://nwmichl.net/2021/06/28/chatops-with-python-fastapi/
# 远程访问

import time

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    # 'http://localhost',
    # 'http://localhost:8000',
    '*',
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True, # cors support cookies?
    allow_methods=["*"],    # default: ['GET']
    allow_headers=["*"],
)

@app.get('/')
async def root():
    return {'message': 'hello world'}

# uvicorn demo11:app --host 0.0.0.0 --reload

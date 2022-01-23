from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .utils.error import load_exception_handler
import os, importlib

app = FastAPI()

# cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_exception_handler(app) # custom handle exception

# automatically load router from app/routers
for router_file in os.listdir('app/routers'):
    if router_file.endswith('.py') and router_file != '__init__.py':
        pkg = f'app.routers.{os.path.splitext(router_file)[0]}'
        router = importlib.import_module(pkg).router
        app.include_router(router, prefix='/api')


@app.get('/')
def index():
    return {
        'project': 'sft',
        'version': '2022.1.23.0',
    }

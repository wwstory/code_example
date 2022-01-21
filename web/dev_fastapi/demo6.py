from fastapi import Form, FastAPI, File, UploadFile
from pydantic import BaseModel
import json

app = FastAPI()

# curl -H "Content-Type: application/json" -F 'data={"name": "建立空中拦截区","scenario_id": 1,"number": "C1","description": "建立空中拦截区"}' -F "file=@test.json" "http://127.0.0.1:8001"
# curl -F 'data={"name": "建立空中拦截区","scenario_id": 1,"number": "C1","description": "建立空中拦截区"}' -F "file=@test.json" "http://127.0.0.1:8001"

class Item(BaseModel):
    id: int
    name: str


# 表单里同时传数据和file
@app.post('/')
async def root(
    data: str = Form(...,),
    file: UploadFile = File(...,)
):
    print(data)
    print(file.filename)

    item: Item = Item(**json.loads(data))
    print(item)
    return {'message': 'hello world'}

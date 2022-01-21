# https://fastapi.tiangolo.com/zh/tutorial/first-steps/

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'hello world'}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

# uvicorn demo1:app --reload

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
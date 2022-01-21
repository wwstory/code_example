from fastapi import Depends, FastAPI, Header

async def my_verify(token: str = 'token1'):
    print('---yyy:', token)

app = FastAPI(dependencies=[Depends(my_verify)])

async def verify_token(x_token: str = Header(None)):
    print('---xxx:', x_token)

# @app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
@app.get("/", dependencies=[Depends(verify_token)])
async def read_items():
    return [{"item": "Foo"}, {"item": "Bar"}]
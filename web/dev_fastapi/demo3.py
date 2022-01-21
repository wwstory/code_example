from typing import Optional

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

    # 添加example到文档，方式1
    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "name": "Foo",
    #             "description": "A very nice Item",
    #             "price": 35.4,
    #             "tax": 3.2,
    #         }
    #     }


@app.put("/items/{item_id}")
async def update_item(
    item_id: int,
    item: Item = Body(
        ...,
        # 添加example到文档，方式2
        # example={
        #     "name": "Foo",
        #     "description": "A very nice Item",
        #     "price": 35.4,
        #     "tax": 3.2,
        # },
    ),
):
    results = {"item_id": item_id, "item": item}
    return results
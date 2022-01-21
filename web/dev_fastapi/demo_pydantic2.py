from typing import Optional, List
from pydantic import BaseModel

class Item(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    tax: float = 10.5
    tags: List[str] = []

items = {
    "foo": {"name": "Foo", "price": 50.2, "tax": 10.5},
}

new_item: Item = Item(name="Foo", price=12.5)               # 请求的数据
stored_item_model = Item(**items['foo'])                    # 模仿，查数据库
update_data = new_item.dict(exclude_unset=True)             # 挑出传入的，排除默认参数
updated_item = stored_item_model.copy(update=update_data)   # 部分修改

print(new_item)
print(stored_item_model)
print(update_data)
print(updated_item)

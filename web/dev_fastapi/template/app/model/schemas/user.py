from pydantic import Field, BaseModel

# from .base_model import BaseModel


class User(BaseModel):
    username: str = Field(...)
    password: str = Field(...)

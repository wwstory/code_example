import pydantic
from pydantic import Field
from datetime import datetime
from bson import ObjectId


class BaseModel(pydantic.BaseModel):
    id: int = Field(...)
    created_at: datetime = Field(...)
    updated_at: datetime = Field(...)
    deleted_at: datetime = Field(...)


class PyObjectId(ObjectId):
    '''
    将mongodb的_id字段对应的ObjectId类型与str类型转换
    '''
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class Datetime(datetime):
    '''
    将date类型转为datetime类型
    '''
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, t):
        try:
            t = datetime.strptime(t, '%Y-%m-%d')
        except:
            raise ValueError("Invalid date")
        return t

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


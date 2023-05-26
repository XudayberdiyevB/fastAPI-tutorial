from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

from app import models, database

models.Base.metadata.create_all(bind=database.engine)
app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def base():
    return {"hello": "Hello world."}


@app.get("/items/{item_id}/{item_name}")
def read_item(item_id: int, item_name: str, q: Union[str, None] = None):
    return {
        "item_id": item_id,
        "name": item_name,
        "q": q
    }


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

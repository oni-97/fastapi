from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel, Field


class SportShop(BaseModel):
    name: str
    url: str


class Item(BaseModel):
    name: str = Field(min_length=4, max_length=12)
    description: Optional[str] = None
    price: int
    tax: Optional[float]


class Data(BaseModel):
    sport_shop: Optional[SportShop] = None
    items: List[Item]


app = FastAPI()


@app.get("/")
async def index():
    return {"Hello": "World"}


@app.get("/sports/soccer")
async def sport():
    return {"sport_name": "soccer id very fun"}


@app.get("/sports/{sport_name}")
async def sport(sport_name: str):
    return {"sport_name": sport_name}


@app.get("/food/")
async def food(food_name: str = "curry", food_price: int = 100):
    return {"food_name": food_name, "food_price": food_price}


@app.get("/food/{food_name}")
async def food(food_name: str, food_price: int = 100):
    return {"food_name": food_name, "food_price": food_price}


@app.get("/drink/")
async def food(drink_name: Optional[str] = None, drink_price: Optional[int] = None):
    return {"drink_name": drink_name, "drink_price": drink_price}


@app.post("/items/")
async def create_item(item: Item):
    return {"message": f"{item.name}は{(int)(item.price*item.tax)}円"}


@app.post("/data/")
async def data(data: Data):
    return {"data": data}

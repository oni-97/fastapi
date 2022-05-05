from fastapi import FastAPI

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

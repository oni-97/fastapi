from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    return {"Hello": "World"}


@app.get("/sports/{sport_name}")
async def sport(sport_name: str):
    return {"sport_name": sport_name}

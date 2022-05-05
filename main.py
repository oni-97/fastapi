from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    return {"Hello": "World"}


@app.get("/sports/{sport_name}")
async def sport(sport_name):
    return {"sport_name": sport_name}

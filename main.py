from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Welcome to TestAPIFramework"}

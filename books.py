from fastapi import FastAPI

app=FastAPI()



@app.get("/read_api/{name}")
async def read_api(name: str):
    return {"Hello":name}

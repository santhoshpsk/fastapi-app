from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
async def root():
    return {"my-node": os.getenv("node_name", "Not Found")}
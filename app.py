from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn
import os

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World1"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


# backend/app/main.py

from fastapi import FastAPI # type: ignore
from pydantic import BaseModel # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore
from .azure_search import search_azure

app = FastAPI()

origins = [
    "http://localhost",  # 允许从 localhost 访问
    "http://localhost:8080",  # 允许从 localhost:3000 访问
    "*",  # 允许所有域
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 允许的源
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有方法，包括 OPTIONS
    allow_headers=["*"],  # 允许所有头部
)

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.post("/query")
async def query(request: QueryRequest):
    answer = search_azure(request.query)
    return {"answer": answer}

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000)

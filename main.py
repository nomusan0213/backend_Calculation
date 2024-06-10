from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Simple arithmetic operations. Use /add, /subtract, /multiply, /divide endpoints."}

@app.get("/add/")
def add(a: int, b: int):
    return {"result": a + b}

@app.get("/subtract/")
def subtract(a: int, b: int):
    return {"result": a - b}

@app.get("/multiply/")
def multiply(a: int, b: int):
    return {"result": a * b}

@app.get("/divide/")
def divide(a: int, b: int):
    if b == 0:
        return {"result": "未定義"}
    return {"result": a / b}

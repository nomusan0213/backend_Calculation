from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Simple arithmetic operations. Use /add, /subtract, /multiply, /divide endpoints"}

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
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    return {"result": a / b}


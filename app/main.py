from fastapi import FastAPI #type: ignore[import]
from app.routes import router

app =FastAPI(title = "Student Management API")

@app.get("/")

def home():
        return {"message" : "Welcome to the Student Management API page"}
app.include_router(router)
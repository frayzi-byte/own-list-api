import uvicorn
from fastapi import FastAPI, status, Depends, HTTPException
from app.routers import task_routers, user_routers
from app.db import ping_db, init_db
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await ping_db()
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(task_routers.router)
app.include_router(user_routers.router)

@app.get("/")
def hello_world():
    return {"message" : "Hello world!"}

if __name__ == "__main__":
    uvicorn.run(app, reload=True)
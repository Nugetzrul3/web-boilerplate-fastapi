from fastapi import FastAPI
from .auth import auth

from .models import engine, SQLModel

app = FastAPI()

app.include_router(auth)

SQLModel.metadata.create_all(engine)


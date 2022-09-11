from fastapi import FastAPI, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session

from . import models
from .database import engine
from .routes import users, posts

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(posts.router)
app.include_router(users.router)

@app.get("/")
def root():
    return "Hello Bloggers!!! Visit /docs for API documentation."




from fastapi import FastAPI

from . import models
from .database import engine
from .routes import users, posts, auth, vote

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return "Hello Bloggers!!! Visit /docs for API documentation."




from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World!!!"}

@app.get("/posts")
def get_posts():
    return {"data": "List of blog posts"}

@app.post("/createposts")
def create_posts(post: Post):
    print(post.dict())
    return "new post created"
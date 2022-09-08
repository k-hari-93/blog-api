from gettext import find
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from random import randrange

def find_post(id):
    for post in my_posts:
        if post["id"] == id:
            return post

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [
    {
        "id": 1,
        "title": "Favourite Drinks", 
        "content": "Tea and Coffee", 
        "published": True, 
        "rating": "4"
    },
    {
        "id": 2,
        "title": "Favourite Passtimes", 
        "content": "Books and Music", 
        "published": False, 
        "rating": "5"
    }
]

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World!!!"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return { "data": post_dict }

@app.get("/posts/{id}")
def get_post(id: int):
    return { "data": find_post(id) }
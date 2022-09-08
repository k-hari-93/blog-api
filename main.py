from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
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
        "title": "Favourite Pastimes", 
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

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return { "data": post_dict }

@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with {id} was not found")
    return { "data": post }
from uuid import uuid4 as uuid
from datetime import datetime
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

# ToDo Model

class ToDo(BaseModel):
    id: Optional[str] = None
    content: str
    created_at: datetime = datetime.now()
    completed: bool = False
    completed_at: Optional[datetime] = None


app = FastAPI()

posts = []

@app.get("/")
def get_todos():
    return {"data": posts}

@app.post("/")
def create_post(post: ToDo):
    post.id = str(uuid())
    posts.append(post.model_dump())
    return post

@app.put("/{id}")
def update_post(id: str, post: ToDo):
    for index, p in enumerate(posts):
        if p["id"] == id:
            post.id = id
            posts[index] = post.model_dump()
            return post
    return {"error": "ToDo not found"}

@app.delete("/{id}")
def delete_post(id: str):
    for index, p in enumerate(posts):
        if p["id"] == id:
            del posts[index]
            return {"message": "ToDo deleted"}
    return {"error": "ToDo not found"}
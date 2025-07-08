from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/blog')
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
	if published:
		return {"data": f"Getting {limit} published blog"}
	else:
		return {"data": f"Getting {limit} unpublished blog"}

@app.get('/blog/unpublished')
def unpublished():
	return {"data": "all unpublished blog"}

@app.get('/blog/{id}')
def show(id: int):
	return {"data": id}

@app.get('/blog/{id}/comments')
def comments(id: int):
	return {"data": {'1', '2'}}

class Blog(BaseModel):
	title: str
	body: str
	published: Optional[bool] = None 

@app.post('/blog')
def create_blog(request: Blog):
	return request
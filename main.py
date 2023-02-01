from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "he to madasdsadasdy API"}


@app.get("/posts")
def get_posts():
    return {"data": "This is your post"}


@app.post("/createposts")
def create_posts(payLoad: dict = Body(...)):
    print(payLoad)
    return {"new_post": f"title {payLoad['title']} content: {payLoad['content']}"}
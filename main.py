from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class Item(BaseModel):
    id:int
    name:str
    description:str
    price:int
    on_offer:bool
    

@app.get('/')
def index():
    return{"message":"hello world"}

@app.get('/greet/{name}')
def greet_name(name:str):
   return {"greeting":f"hello {name}"}


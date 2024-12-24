from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

inventory = {}



# <--------------------------------------Get Request------------------------------------>
@app.get("/")
def home():
    return {"Message": "This is the home page"}

@app.get("/about/")
def about():
    return {"Message": "This is the about page"}

# <--- Path Parameters --->
@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(description="The ID of the item to get", gt=0)): 
    return inventory[item_id]

@app.get("/get-by-name")
def get_item(name: str = None):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {"Data": "Not Found"}

# # <-----Query Parameters----->
# @app.get("/get-by-name")
# def get_item(*, name: Optional[str] = None, test: int):
#     for item_id in inventory:
#         if inventory[item_id]["name"] == name:
#             return inventory[item_id]
#     return {"Data": "Not Found"}

# <-----Querey Parameters with path parameters----->
# @app.get("/get-by-name/{item_id}")
# def get_item(*, item_id: int, name: Optional[str] = None, test: int):
#     for item_id in inventory:
#         if inventory[item_id]["name"] == name:
#             return inventory[item_id]
#     return {"Data": "Not Found"}



# <--------------------------------------Post Request------------------------------------>
@app.post("/create-item/{item_id}")
def create_ites(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item ID already exists"}
    
    inventory[item_id] = item
    return inventory[item_id]
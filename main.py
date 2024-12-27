from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
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
    raise HTTPException(status_code=404, detail="Item name not found")

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
        raise HTTPException(status_code=400, detail="Item ID already exists")
    
    inventory[item_id] = item
    return inventory[item_id]



# <--------------------------------------Put Request------------------------------------>
@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item ID does not exist")
    
    if item.name != None:
        inventory[item_id].name = item.name
    if item.price != None:
        inventory[item_id].price = item.price
    if item.brand != None:
        inventory[item_id].brand = item.brand
    return inventory[item_id]



# <--------------------------------------Delete Request------------------------------------>
@app.delete("/delete-item")
def delete_item(item_id: int = Query(..., description="The ID of the item to delete", gt=0)):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item ID does not exist")
    
    del inventory[item_id]
    return {"Message": "Item Deleted Successfully"}
from fastapi import FastAPI, Path

app = FastAPI()

inventory = {
    1: {
        "name": "Milk",
        "price": 2.99,
        "brand": "Dairy Farmers"
    },
    2: {
        "name": "Bread",
        "price": 2.50,
        "brand": "Wonder White"
    },
}

@app.get("/")
def home():
    return {"Message": "This is the home page"}

@app.get("/about/")
def about():
    return {"Message": "This is the about page"}

@app.get("/items/{item_id}")
def get_item(item_id: int = Path(description="The ID of the item to get", gt=0, lt=3)): 
    return inventory[item_id]
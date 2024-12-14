from typing import Union

from fastapi import FastAPI

app = FastAPI()
items = []
#------------------------------------------------------------
#get
@app.get("/") 
def create_item(): 
    
    return {"":items}
#------------------------------------------------------------
#get
@app.get("/user{item_id}")
def create_item(item_id: str):
    items.append(item)
    return items
#------------------------------------------------------------
#post
@app.post("/user/{item_id}") 
def create_item(item_id: str): 
    items.append(item_id) 
    return {"item_id": item_id
    
    }
#------------------------------------------------------------
#delete 
@app.delete("/user/{item_id}") 
def create_item(item_id: str): 
    items.remove(item_id) 
    return {"item_id": item_id
    
    }
#------------------------------------------------------------
#put
@app.put("/user/{item_id}") 
def create_item(item_id: str): 
    items.append(item_id) 
    return {"item_id": item_id
    
    }
#------------------------------------------------------------

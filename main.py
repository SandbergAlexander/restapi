from typing import Union

from fastapi import FastAPI, HTTPException
app = FastAPI()
items = ["alexander", "test-name", "sato"] 

#------------------------------------------------------------
#get
@app.get("/") 
def get_all_items(): 
    return items
#------------------------------------------------------------
#get
@app.get("/user/{item_id}") 
def get_item(item_id: str): 
    if not item_id: 
        raise HTTPException(status_code=400, detail="Item ID is required") 
        items(item_id) 
        return {"user"} 

    
#------------------------------------------------------------
#post
@app.post("/user/{item_id}") 
def create_item(item_id: str): 
  
        items.append(item_id) 
        return { item_id} 
#delete
#------------------------------------------------------------
@app.delete("/user/{item_id}") 
def delete_item(item_id: str): 
        items.remove(item_id) 
        return {"Delete":item_id}
#------------------------------------------------------------
#put
@app.put("/user/{item_id}") 
def change_item(item_id: str): 
    items.append(item_id) 
    return {"item_id": item_id
    
    }
#------------------------------------------------------------

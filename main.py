from typing import Union

from fastapi import FastAPI, HTTPException
app = FastAPI()
items = ["alexander", "Alexander", "sato","benny"] 

#------------------------------------------------------------
#get
@app.get("/",status_code=200) 
def get_all_items(): 
    return items
#------------------------------------------------------------
#get
@app.get("/user/{item_id}",status_code=200) 
def get_item(item_id: str):  
        items.index(item_id) 
        return {"user":item_id} 
#------------------------------------------------------------
#post
@app.post("/user/{item_id}",status_code=201) 
def create_item(item_id: str): 
        items.append(item_id) 
        return {item_id} 
#delete
#------------------------------------------------------------
@app.delete("/user/{item_id}",status_code=204) 
def delete_item(item_id: str): 
        items.remove(item_id) 
        return {}
#------------------------------------------------------------
#put
@app.put("/user/{item_id}",status_code=201) 
def change_item(item_id: str): 
    items.append(item_id) 
    return {"item_id": item_id}
#------------------------------------------------------------
 
from typing import Union

from fastapi import FastAPI

app = FastAPI()
ordlista = ["hej","hejdå"]
testa = ordlista[0]
print (testa)
#------------------------------------------------------------
#get
@app.get("/")
def read_root():
    return {""}
#------------------------------------------------------------
#get
@app.get("/user")
def read_root():
    return {"hej"}
#------------------------------------------------------------
#post
@app.post("/user")
def post_root():
    return {ordlista.append("hej")}
#------------------------------------------------------------
#delete 
@app.delete("/user")
def delete_root():
    return {"hej"}
#------------------------------------------------------------
#put
@app.put("/user")
def put_root():
    return {"hej"}
#------------------------------------------------------------

@app.get("/",status_code=200) 
def get_all_items(): 
    return items
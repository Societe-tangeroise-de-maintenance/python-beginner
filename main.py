from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app= FastAPI()

ilist={}

class Item(BaseModel):
    id:str
    name:str
    price:float
    description:str

#Create an item
@app.post("/items/{id}")
def createfunct(item:Item):
                id= item.id
                if id in ilist:
                    raise HTTPException(status_code=400,
                                detail=f'The item {id} already exists')
                else:
                    ilist[id] = item.dict()
                    return{'message': f'Item {id} successfully added'}         
#Give the whole list
@app.get("/items/")
def listfunct():
    return(ilist)

#Get item by id
@app.get('/ilist/{id}')
def findfunct(id:str):
        if id in ilist:
              return ilist[id]
        else:
            raise HTTPException(status_code=400,
                                detail=f'There is no item by the id: {id}') 
             
#Delete by id
@app.delete("/ilist/{id}")
def delfunct(id:str):
        if id not in ilist:
              raise HTTPException(status_code=400,
                             detail=f'There is no item by the id: {id}')
        else:
               del ilist[id]
               return{'message': f'Item {id} successfully deleted'}

#Update
@app.put("/ilist/{id}")
def upfunct(item:Item):
        id= item.id
        if id in ilist:
            ilist[id]=item.dict()
            return{'message': f'Item {id} successfully updated'}
        else:
            raise HTTPException(status_code=400,
                                detail=f'The item {id} does not exist')
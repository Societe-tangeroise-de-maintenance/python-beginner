from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel

app= FastAPI()

itemlist={}

class Item(BaseModel):
    id:int
    name:str
    price:float
    description:str

class updateditem(BaseModel):
    name: Optional[str]= None
    price:Optional[float]=None
    description:Optional[str]= None

#Create an item
@app.post("/itemlist/")
def createItem(item:Item):
                id= item.id
                if id in itemlist:
                    raise HTTPException(status_code=400,
                                detail=f'The item {id} already exists')
                else:
                    itemlist[id] = item.dict()
                    return{'message': f'Item {id} successfully added!'}         
#Give the whole list
@app.get("/itemlist/")
def listAllItems():
    return(itemlist)

#Get item by id
@app.get('/itemlist/{id}')
def searchByID(id:int):
        if id in itemlist:
              return itemlist[id]
        else:
            raise HTTPException(status_code=400,
                                detail=f'There is no item by the id: {id}') 
             
#Delete by id
@app.delete("/itemlist/{id}")
def deleteItem(id:int):
        if id not in itemlist:
              raise HTTPException(status_code=400,
                             detail=f'There is no item by the id: {id}')
        else:
               del itemlist[id]
               return{'message': f'Item {id} successfully deleted!'}

#Update
@app.put("/itemlist/{id}")
def updateItem(id:int, item:updateditem):
        if id not in itemlist:
               raise HTTPException(status_code=400,
                                detail=f'The item {id} does not exist')
        else:
             if item.name!=None:
                itemlist[id]["name"]=item.name
             if item.price!=None:
                 itemlist[id]["price"]=item.price
             if item.description!=None:
                itemlist[id]["description"]=item.description
             return {'message': f'Item {id} successfully updated!'}
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app= FastAPI()

itemlist={}

class Item(BaseModel):
    id:str
    name:str
    price:float
    description:str

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
def searchByID(id:str):
        if id in itemlist:
              return itemlist[id]
        else:
            raise HTTPException(status_code=400,
                                detail=f'There is no item by the id: {id}') 
             
#Delete by id
@app.delete("/itemlist/{id}")
def deleteItem(id:str):
        if id not in itemlist:
              raise HTTPException(status_code=400,
                             detail=f'There is no item by the id: {id}')
        else:
               del itemlist[id]
               return{'message': f'Item {id} successfully deleted!'}

#Update
@app.put("/itemlist/{id}")
def updateItem(updateditem:Item):
        id= updateditem.id
        if id in itemlist:
            itemlist[id]=updateditem.dict()
            return{'message': f'Item {id} successfully updated!'}
        else:
            raise HTTPException(status_code=400,
                                detail=f'The item {item.id} does not exist')
# Problem: Simple CRUD (Create, Read, Update, Delete) API with FastAPI - STM CODING CHALLENGE
## FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

## All devs within the STM organization can take on this challenge for learning purposes. Create your own branch, once you're done create a review and add me to it (SDDoSx)

## Problem Statement

Your task is to create a simple FastAPI application with the following endpoints:

1. GET /items/: Returns a list of items.
2. GET /items/{item_id}: Returns the item with the given item_id.
3. POST /items/: Adds a new item.
4. PUT /items/{item_id}: Updates the item with the given item_id.
5. DELETE /items/{item_id}: Deletes the item with the given item_id.

For simplicity, an "item" is represented as a dictionary with the following structure:

```
{
    "id": "string",
    "name": "string",
    "price": "float",
    "description": "string"
}
```
And you should use a list to store the items.

## Instructions

1. Install FastAPI and uvicorn (an ASGI server) using pip. You can do this using the following command:
bash

```
pip install fastapi uvicorn
```

2. Create a new file called main.py and import FastAPI:

```
from fastapi import FastAPI

app = FastAPI()
```

3. Define a list items to store the items.

4. Define the FastAPI endpoints as described in the problem statement. You can use the @app.route() decorator to define an endpoint. For example, a simple GET endpoint may look like this:

```
@app.get("/items/")
async def read_items():
    return items
```

5. Use the if __name__ == "__main__": idiom to run the application using uvicorn when the script is invoked directly:

```
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

## Hints:

* To extract path parameters, you can include them in the function parameters. For example, to extract the item_id from the path, you can define a function like this:

```
@app.get("/items/{item_id}")
async def read_item(item_id: str):
    ...
    
```

* FastAPI automatically converts Python exceptions to HTTP 500 responses. To return a different response code, you need to raise a fastapi.HTTPException.

## Bonus:

1. Add data validation: The POST and PUT endpoints should verify that the input data is valid (e.g., all fields are present and have the correct types) and return an HTTP 400 response if the data is invalid.

2. Use Pydantic models: FastAPI integrates seamlessly with Pydantic models. These models allow you to define the data structures and automatically take care of data validation, serialization, and documentation.

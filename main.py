# main.pr is the main file and containts the FastAPI app

from fastapi import FastAPI

shodan_api = FastAPI()


@shodan_api.get("/")
async def read_root():
    return {"message": "Hello human"}


# Now we will create operations for the API to perform POST, GET, PUT, DELETE
@shodan_api.post("/items/")
async def create_item(item: dict):
    items.append(item)
    return item


@shodan_api.get("/items/")
async def read_items():
    return items


@shodan_api.get("/items/{item_id}")
async def read_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    return {"message": "Item not found"}


@shodan_api.put("/items/{item_id}")
async def update_item(item_id: int, item: dict):
    for i, current_item in enumerate(items):
        if current_item["id"] == item_id:
            items[i] = item
            return item
    return {"message": "Item not found"}


@shodan_api.delete("/items/{item_id}")
async def delete_item(item_id: int):
    for i, item in enumerate(items):
        if current_item["id"] == item_id:
            del items[i]
            return {"message": "Item deleted"}
        return {"message": "Item not found"}

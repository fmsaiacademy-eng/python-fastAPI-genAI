from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/itemsList")
def read_items():
    return [
        {"id": 1, "name": "Apple", "price": 1.5, "quantity": 10},
        {"id": 2, "name": "Banana", "price": 0.8, "quantity": 15}
    ]

@app.get("/cityList")
def read_items():
    return [
        {"id": 1, "name": "Bangalore"},
        {"id": 2, "name": "Chennai"}
    ]
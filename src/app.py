from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def load_index():

    return {"Hello": "World"}
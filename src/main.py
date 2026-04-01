from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def load_index():

    return {"Hello": "World"}


@app.get("/task")
def show_tasks():
    
    return{"task1":"Run my first fastapi application",
           "task2":"Used port 8011 for the first time to run an application"}
    
@app.get('/api/v1/hello-world/')
def read_hello_world():
    
    return {"What":"road","where":"Kubernetes","version":"v1"}
    
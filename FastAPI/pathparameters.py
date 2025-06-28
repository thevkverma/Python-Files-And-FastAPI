from fastapi import FastAPI

app = FastAPI()

@app.get("/item/{Item}")
def path_fun(Item):
    var_name = {"path variable": Item}
    return (var_name)
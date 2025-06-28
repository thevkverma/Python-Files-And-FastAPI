from unittest.util import _MAX_LENGTH
from fastapi import FastAPI, Path, Query
from enum import Enum
from typing import Union

class choice_name(str, Enum):
    one = "one"
    two = "two"
    three = "three"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: choice_name):
    return(model_name)

@app.get("/model/{model_name}")
async def get_model(model_name: choice_name):
    if model_name.value == "one":
        return {"model_name": model_name, "message": "You chose the first model!"}
    if model_name.value == "two":
        return {"model_name": model_name, "message": "You chose the second model!"}
    
    return{"model_name": model_name, "message": "You chose the third model!"}
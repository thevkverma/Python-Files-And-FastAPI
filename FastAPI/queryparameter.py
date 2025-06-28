from unittest.util import _MAX_LENGTH
from fastapi import FastAPI, Path, Query
from enum import Enum
from typing import Union
from pydantic import BaseModel

app = FastAPI()

@app.get("/query")
def query_fun(name: str, roll_no: int):
    var_name = {'name': name, 'roll no': roll_no}
    return(var_name)
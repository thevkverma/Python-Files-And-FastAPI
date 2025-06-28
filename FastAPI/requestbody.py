from unittest.util import _MAX_LENGTH
from fastapi import FastAPI, Path, Query
from enum import Enum
from typing import Union
from pydantic import BaseModel

class schema1(BaseModel):
    name:str
    Class:str
    roll_no:int

app = FastAPI()

@app.post("/req/")
async def create_item(item: schema1):
    return item
from unittest.util import _MAX_LENGTH
from fastapi import FastAPI, Path, Query, Form, File, UploadFile, HTTPException
from enum import Enum
from typing import Union
from pydantic import BaseModel

app = FastAPI()

items = [1,2,3,4,5]
@app.get("/error/handling")
async def handle_error(item: int):
    if item not in items:
        return HTTPException(status_code = 400, detail = "Item is not equal to 2 try another value!!!")
    return {"value": item}
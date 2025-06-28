from unittest.util import _MAX_LENGTH
from fastapi import FastAPI, Path, Query, Form
from enum import Enum
from typing import Union
from pydantic import BaseModel

app = FastAPI()

@app.post("/form/data")
async def form_data(username : str = Form(), password : str = Form()):
    return({"username": username, "password": password})
from unittest.util import _MAX_LENGTH
from fastapi import FastAPI, Path, Query, Form, File, UploadFile
from enum import Enum
from typing import Union
from pydantic import BaseModel

app = FastAPI()

@app.post("/file/data")
async def file_bytes_len(file: bytes = File()):
    return({"file": len(file)})

@app.post("/file/upload")
async def file_upload(file : UploadFile):
    return({"file" : file})

@app.post("/file/name")
async def file_upload(file : UploadFile):
    return({"file_name": file.filename, "file_content_name": file.content_type})
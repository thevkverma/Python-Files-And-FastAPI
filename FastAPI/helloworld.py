from fastapi import FastAPI

hello_world = FastAPI()

@hello_world.get("/hello")
async def root():
    return {"message": "Hello from vivek side..!"}

@hello_world.get("/hey")
async def vivek():
    return {"message": "hey, how are you..!"}
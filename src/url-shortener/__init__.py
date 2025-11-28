from fastapi import FastAPI

app = FastAPI()


def hello():
    print("<h1>Hello world")


@app.get("/")
async def root():
    return "Hello world"
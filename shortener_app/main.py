from fastapi import FastAPI # type: ignore


app = FastAPI()


@app.get("/")
def read_root():
    return "Welcome to the URL shortener API :)"

'''
@app.get("/{url_key}")
@app.post("/url")
@app.get("/admin/{secret_key}")
@app.delete("/admin/{secret_key}")
'''
import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_list():
    return [1,2,3,4]

@app.get("/contact", response_class=HTMLResponse)
async def get_list():
    return """
        <h1> hello world khristopher! </h1>
        <p> the best programmer in the world </p>
    """

async def run():
    store.get_categories()

if __name__ == '__main__':
    run()
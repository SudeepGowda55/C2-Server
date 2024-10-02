from fastapi import FastAPI
from contextlib import asynccontextmanager
from utils import RED, startup_banner

@asynccontextmanager
async def lifespan_event(app: FastAPI):
    startup_banner()
    yield
    print(f"{RED}Server is shutting down...")

app = FastAPI(lifespan=lifespan_event)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=3000)
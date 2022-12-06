from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from uvicorn import run

from routes import router

app = FastAPI()

@app.get("/", response_class=RedirectResponse, tags=["Index"])
def index():
    return "/docs"

app.include_router(router)

if __name__ == "__main__":
    run("app:app", reload=True)
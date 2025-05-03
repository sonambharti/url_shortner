from fastapi import FastAPI
from app.api.routes import auth, user
import uvicorn

app = FastAPI()
app.include_router(auth.router)
app.include_router(user.router)


@app.get("/")
def root():
    return {"message": "Welcome to the URL Shortener"}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
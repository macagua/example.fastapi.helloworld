from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()


@app.get("/")
async def root():
    """A simple hello world endpoint."""
    return {"message": "Hello World"}

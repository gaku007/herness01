"""FastAPI application for herness."""
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def hello_world() -> dict[str, str]:
    """Return Hello World message.
    
    Returns:
        dict: A dictionary containing the message "Hello World"
    """
    return {"message": "Hello World"}

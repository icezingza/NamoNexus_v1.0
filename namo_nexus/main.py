import uvicorn
from namo_nexus.api.http_server import app

# For uvicorn namo_nexus.main:run
run = app

def start():
    """Entry point for script execution."""
    uvicorn.run("namo_nexus.main:run", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    start()

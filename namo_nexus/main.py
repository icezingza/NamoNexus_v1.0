# namo_nexus/main.py
import uvicorn


def run() -> None:
    uvicorn.run(
        "app.api.gateway:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )


if __name__ == "__main__":
    run()

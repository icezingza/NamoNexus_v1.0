import traceback
try:
    from app.api.gateway import app
    print("Import success")
except Exception:
    traceback.print_exc()

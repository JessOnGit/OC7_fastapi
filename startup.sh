# Startup file, fastapi

# python -m uvicorn main:app  --reload
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
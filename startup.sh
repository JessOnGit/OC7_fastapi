# Startup file, fastapi

python -m uvicorn main:app  --reload
# python -m gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
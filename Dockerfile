FROM python:3.8.5-slim

COPY requirements.txt .
RUN python -m pip install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN python -m pip install -r requirements.txt
COPY . .

RUN python scripts/create_database.py

# using $PORT for deploy to heroku:
CMD uvicorn main:app --host 0.0.0.0 --port $PORT

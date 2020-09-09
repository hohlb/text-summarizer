FROM python:3.8.5-slim

WORKDIR /app

# install python packages
COPY requirements.txt .
RUN python -m pip install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN python -m pip install -r requirements.txt

# copy our source files
COPY . .

# create database
RUN python scripts/create_database.py

# force the download of the language model (will be downloaded on first use) and cache it
ENV TORCH_HOME=/app/.torch
RUN python -c "from src.summarize import summarize_text; summarize_text('This is an example input text.')"

# serve the the REST API
# (using $PORT environment variable for deployments to heroku):
CMD uvicorn main:app --host 0.0.0.0 --port $PORT

FROM python:3.8.5-slim

WORKDIR /app

# install python packages
COPY requirements.txt .
RUN python -m pip install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN python -m pip install -r requirements.txt

# import our source files
COPY . .

# create the database that holds the summarized texts
RUN python scripts/create_database.py

# force the download of the language model (which will be downloaded on first use) to cache it
#
# $TORCH_HOME gets used as the base directory for the the transformers library cache,
# see https://huggingface.co/transformers/installation.html?highlight=transformers_cache#caching-models
ENV TORCH_HOME=/app/.torch
RUN python -c "from src.summarize import summarize_text; summarize_text('This is an example input text to trigger the language model download.')"

# serve the the REST API
ENV PORT 8000
EXPOSE $PORT
CMD uvicorn main:app --host 0.0.0.0 --port $PORT

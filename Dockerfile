FROM python:3.8.5-slim AS install
WORKDIR /install
COPY requirements.txt .
# the --user flag creates a ".local" directory
RUN python -m pip install --user torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN python -m pip install --user -r requirements.txt
COPY . .

FROM python:3.8.5-slim AS runtime
WORKDIR /app
COPY --from=install /install/.local ./.local
# ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", $PORT]
# heroku uses the following
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", $PORT]

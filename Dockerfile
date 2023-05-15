FROM python:3.10-slim

WORKDIR /app

COPY utils/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "run.py"]

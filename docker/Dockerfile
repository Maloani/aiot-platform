FROM python:3.9

WORKDIR /app

COPY ../backend /app
COPY ../model /app/model

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
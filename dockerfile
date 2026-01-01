FROM python:3.10-slim

WORKDIR /app

COPY car.py .

CMD ["python", "car.py"]
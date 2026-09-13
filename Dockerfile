FROM python:3.9-slim
WORKDIR /app
COPY . /app
EXPOSE 5000
CMD ["python", "app.py"]

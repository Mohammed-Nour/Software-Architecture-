FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install Flask
RUN pip install flask_sqlalchemy
EXPOSE 5002
CMD ["python", "app.py"]

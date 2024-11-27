FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install Flask requests
RUN pip install flask_sqlalchemy
EXPOSE 5000
CMD ["python", "app.py"]

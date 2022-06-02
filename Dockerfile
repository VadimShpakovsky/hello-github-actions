FROM python:3.9-slim-buster

RUN pip install --upgrade pip && \
    pip install pipenv

WORKDIR /app

COPY . .

RUN pipenv sync

EXPOSE 8080

CMD ["pipenv", "run", "python", "server.py"]

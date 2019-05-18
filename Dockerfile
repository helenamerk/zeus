FROM python:latest

COPY . /app

WORKDIR /app

RUN pip install pipenv && pipenv --python 3.7 && pipenv install

ENV FLASK_APP=./zeus

ENV FLASK_ENV=production

ENV PORT=80

CMD ["pipenv", "run", "flask", "run", "--host", "0.0.0.0", "--port", "80"]

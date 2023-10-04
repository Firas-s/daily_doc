
FROM python:3.9

ENV PYTHONUNBUFFERED True

COPY runs/yext/requirements.txt ./

RUN pip install --upgrade pip
RUN pip install keyrings.google-artifactregistry-auth
RUN pip install -r requirements.txt

ENV APP_HOME /app
WORKDIR $APP_HOME

COPY runs/yext/app.py ./
COPY runs/yext/src/* ./src/

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 --reload app:app
FROM python:2.7.18-alpine3.11 AS build

LABEL maintainer="Antanas Domarkas"

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt
RUN python init_db.py

EXPOSE 3111

ENTRYPOINT [ "python", "app.py" ]

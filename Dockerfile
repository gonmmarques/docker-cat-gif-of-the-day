FROM alpine:3.12.1
LABEL maintainer="goncalommarques"

RUN apk add --update py-pip
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py /usr/src/app
COPY templates /usr/src/app/templates

WORKDIR /usr/src/app/templates
RUN ls


EXPOSE 5000

CMD ["python3", "/usr/src/app/app.py"]
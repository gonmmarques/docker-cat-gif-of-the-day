FROM alpine:3.12.1
LABEL maintainer="goncalommarques"

RUN apk add --update py-pip
WORKDIR /usr/src/app

COPY . /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python3", "/usr/src/app/app.py"]
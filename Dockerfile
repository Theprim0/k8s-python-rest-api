FROM python:3.8-alpine

WORKDIR /app

RUN apk add curl

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 80

CMD [ "python3", "main.py"]

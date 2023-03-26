FROM python:3.8-slim-buster
EXPOSE 8000
WORKDIR /app

COPY requirements.txt /app
RUN pip3 install -r requirements.txt

COPY . /app
ENTRYPOINT [ "python" ]


CMD [ "manage.py", "runserver" , "0.0.0.0:8000"]


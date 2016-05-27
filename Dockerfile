FROM python:3.5

RUN pip install requests bcrypt flask
RUN mkdir /src
ADD src /src
WORKDIR /src
EXPOSE 5000

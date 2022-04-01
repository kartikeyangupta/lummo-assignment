FROM python:3.8

RUN apt-get update

RUN apt-get install vim

ADD ./application /src/project/

WORKDIR /src/project/

RUN python3 -m venv .testenv

RUN source .testenv/bin/activate

RUN pip install -r requirements.txt

CMD ["python3", "app.py"]

EXPOSE 6000
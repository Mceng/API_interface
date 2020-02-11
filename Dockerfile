FROM python:3.6.0
LABEL maintainer='mocheng'
ENV PYTHONUNBUFFERED 1
RUN mkdir /code

WORKDIR /code

#RUN pip install pip -U
ADD . /code/

RUN pip install -r requirements.txt -i https://pypi.douban.com/simple
CMD ["pytest","run.py"]
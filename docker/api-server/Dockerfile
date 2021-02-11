FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

ADD requirements.txt /tmp/
RUN cd /tmp/ && pip3 install -r requirements.txt

ADD . /tmp/
RUN cd /tmp/ && python3 setup.py install

COPY turbinia/api-server /app
RUN ls -al /app

RUN mkdir /app/evidence

ENV MODULE_NAME=turbiniaapi
ENV VARIABLE_NAME=api
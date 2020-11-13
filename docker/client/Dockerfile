FROM ubuntu:18.04

RUN apt-get update && apt-get -y install \
apt-transport-https \
apt-utils \
ca-certificates \
libterm-readline-gnu-perl \
python3 \
python3-pip \
software-properties-common \
&& rm -rf /var/lib/apt/lists/*

RUN pip3 install pip --upgrade
RUN pip3 install urllib3 cryptography --upgrade

ADD . /tmp/
RUN cd /tmp/ && pip3 install -r requirements.txt
RUN cd /tmp/ && pip3 install -r dfvfs_requirements.txt
RUN cd /tmp/ && python3 setup.py install

ENTRYPOINT ["/usr/local/bin/turbiniactl"]

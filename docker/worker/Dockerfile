FROM ubuntu:18.04

RUN apt-get update && apt-get -y install \
apt-transport-https \
apt-utils \
ca-certificates \
john \
john-data \
libterm-readline-gnu-perl \
python3-dev \
python3-pip \
python3-setuptools \
python3-wheel \
software-properties-common \
sudo \
&& rm -rf /var/lib/apt/lists/*

RUN pip3 install urllib3 cryptography --upgrade
RUN pip3 install turbinia

# Install Plaso
RUN add-apt-repository -y ppa:gift/stable
RUN apt-get -y install plaso-tools --option Acquire::ForceIPv4=true --option Acquire::Retries=100 --option Acquire::http::Timeout=60

# Install Hindsight
RUN pip3 install pyhindsight

RUN useradd -r -s /bin/nologin -G disk turbinia
RUN echo "turbinia ALL = (root) NOPASSWD: /bin/mount,/bin/umount,/sbin/losetup" > /etc/sudoers.d/turbinia

RUN mkdir /etc/turbinia && mkdir -p /mnt/turbinia/ mkdir -p /var/lib/turbinia/ \
&& mkdir -p /etc/turbinia/ && chown -R turbinia:turbinia /etc/turbinia/ \
&& mkdir -p /var/log/turbinia/ && chown -R turbinia:turbinia /mnt/turbinia/ \
&& chown -R turbinia:turbinia /var/lib/turbinia/ \
&& chown -R turbinia:turbinia /var/log/turbinia/

COPY start.sh /home/turbinia/start.sh
RUN chmod +x /home/turbinia/start.sh
USER turbinia
CMD ["/home/turbinia/start.sh"]

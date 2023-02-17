FROM ubuntu:22.04

ARG debian_frontend=noninteractive
SHELL [ "/bin/bash", "-c" ]

RUN cp /etc/apt/sources.list /etc/apt/sources.list.backup && \
    sed -i -r 's,http://(.*).ubuntu.com,http://mirror.us-tx.kamatera.com,' /etc/apt/sources.list

# making sure Python is Python 3
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y --no-install-recommends install \
    python3-dev \
    python3-pip \
    python-is-python3

# making sure we have Intel GPU access
RUN apt-get update && \
    apt-get -y --no-install-recommends install \
    libgl1-mesa-glx \
    libgl1-mesa-dri \
    mesa-utils \
    mesa-utils-extra

# making sure we have MAVSDK
# see https://mavsdk.mavlink.io/main/en/python/quickstart.html#install
RUN python -m pip install --upgrade pip setuptools wheel testresources mavsdk aioconsole

# automatically start in the root directory since our source folder is in /root/src
RUN echo "cd /root" >> ~/.bashrc
FROM ubuntu:16.04
RUN apt-get update && apt-get install -y iputils-ping
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
CMD bash
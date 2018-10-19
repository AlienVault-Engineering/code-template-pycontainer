FROM debian:sid
MAINTAINER AlienVault
RUN apt-get update && apt-get install -y python-pip python  \
    && apt-get clean \
    && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*
RUN mkdir /task
ARG buildVersion
ENV BUILD_VERSION=$buildVersion
COPY . /task
ENTRYPOINT ["/task/run_server.sh"]

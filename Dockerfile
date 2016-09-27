FROM fedora:latest
MAINTAINER mmitti <dev@mail.mmitti.info>
RUN dnf install -y python-pip gcc redhat-rpm-config python3-devel
RUN pip3 install netifaces
RUN dnf install -y curl tar
RUN curl -L https://github.com/coreos/etcd/releases/download/v3.0.10/etcd-v3.0.10-linux-amd64.tar.gz -o etcd-v3.0.10-linux-amd64.tar.gz
RUN tar xzvf etcd-v3.0.10-linux-amd64.tar.gz
RUN mv etcd-v3.0.10-linux-amd64/etcd /bin
COPY run.py /
ENTRYPOINT python3 /run.py

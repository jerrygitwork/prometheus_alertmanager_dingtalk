FROM centos:7

ENV BASEDIR /prometheus_alertmanager_dingtalk/

RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7 \
    && yum install -y epel-release \
    && rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7 \
    && yum install -y git python gcc \
    && yum clean all

ADD . ${BASEDIR}/
WORKDIR ${BASEDIR}/

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && python get-pip.py \
    && rm -rf get-pip.py \
    && pip --no-cache-dir install -r requirements.txt \
    && python setup.py install \
    && mkdir -p /etc/prometheus_alertmanager_dingtalk

CMD [ "prometheus_dingtalk", "--config-file", "/etc/prometheus_alertmanager_dingtalk/prom-dingtalk.conf" ]

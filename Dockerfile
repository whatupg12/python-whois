FROM        ubuntu:16.04

WORKDIR     /opt/python-whois

COPY        . /opt/python-whois/

RUN         apt-get update && apt-get install -y python whois netbase
RUN         python setup.py build && python setup.py install

ENTRYPOINT ["python", "run.py"]
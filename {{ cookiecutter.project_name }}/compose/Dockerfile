FROM abrahamliu/runit-python-web:1.0

COPY requirements/ /tmp/requirements

RUN pip3 install -r /tmp/requirements/production.txt -i https://pypi.douban.com/simple && \
        /bd_build/cleanup.sh

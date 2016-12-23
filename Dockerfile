FROM gw000/keras:1.1.1-py2-tf-cpu
MAINTAINER ioriiod0@gmail.com

RUN pip install git+https://github.com/matthiasplappert/keras-rl.git
RUN pip install -i http://pypi.douban.com/simple/ --trusted-host=pypi.douban.com pandas

ADD . /code
RUN cd /code && python setup.py install

WORKDIR /code


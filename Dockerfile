FROM 10.202.11.142/sfai/auto_encoder
MAINTAINER ioriiod0@gmail.com

RUN pip install git+https://github.com/matthiasplappert/keras-rl.git
RUN pip install -i http://pypi.douban.com/simple/ --trusted-host=pypi.douban.com pandas

ADD . /code
RUN cd /code && python setup.py install

WORKDIR /code


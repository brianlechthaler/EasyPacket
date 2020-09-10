# start from Alpine Linux bleeding edge
FROM alpine:edge
# install pip for python 3.x using apk
RUN apk add py3-pip
# install 3 dependencies with pip
RUN pip install -U pip
RUN pip install -U scapy
RUN pip install -U ipython
# copy contents of this repo into the container
ADD . /opt/easypacket/
# set the CMD to a helpful note followed by and IPython prompt
CMD echo "Read the README if you don't know what to do here." && ipython

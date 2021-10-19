ARG BUILD_FROM
FROM $BUILD_FROM
ENV LANG C.UTF-8

RUN set -xe \
    && apk add --no-cache gcc build-base git i2c-tools nano linux-headers cmake pacman python3 py3-pip python3-dev py-rpigpio


# RUN set -xe \
#     && apk add --no-cache build-base git i2c-tools nano linux-headers pacman python3 \
#     && mkdir /UCTronics_OLED \
#     && mkdir /UCTronics_OLED_dev

#
# install python3
# sudo pip3 install adafruit-circuitpython-ssd1306
# RUN curl -O https://bootstrap.pypa.io/get-pip.py
# RUN python get-pip.py

RUN pip3 install adafruit-blinka
RUN pip3 install adafruit-circuitpython-ssd1306
RUN pip3 install requests
RUN pip3 install RPi.GPIO

#sudo apt-get install python3-pip
#sudo apt-get install python3-pil

# Copy over the C project
COPY /ssd1306/* /UCTronics_OLED/
COPY /python* /UCTronics_OLED_Python

COPY run.sh /
COPY start.sh /
WORKDIR /data
RUN chmod a+x /run.sh
RUN chmod a+x /start.sh

CMD [ "/start.sh" ]
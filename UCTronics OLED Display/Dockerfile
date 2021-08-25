ARG BUILD_FROM
FROM $BUILD_FROM
ENV LANG C.UTF-8

RUN set -xe \
    && apk add --no-cache build-base git i2c-tools nano linux-headers cmake json-c-dev \
    && mkdir /UCTronics_OLED \
    && mkdir /UCTronics_OLED_dev


# RUN set -xe \
#     && apk add --no-cache build-base git i2c-tools nano linux-headers pacman python3 \
#     && mkdir /UCTronics_OLED \
#     && mkdir /UCTronics_OLED_dev

#
# install python3
# sudo pip3 install adafruit-circuitpython-ssd1306
# RUN curl -O https://bootstrap.pypa.io/get-pip.py
# RUN python get-pip.py
# RUN pip3 install adafruit-circuitpython-ssd1306
# RUN pip3 install RPi.GPIO

# sudo apt-get install python3-pip
# sudo apt-get install python3-pil

# Copy over the C project
COPY /ssd1306/* /UCTronics_OLED/

COPY /ssd1306_dev/* /UCTronics_OLED_dev/

COPY run.sh /
WORKDIR /data
RUN chmod a+x /run.sh
CMD [ "/run.sh" ]
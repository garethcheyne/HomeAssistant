ARG BUILD_FROM
FROM $BUILD_FROM
ENV LANG C.UTF-8

RUN set -xe \
    && apk add --no-cache build-base git i2c-tools nano linux-headers \
    && git clone https://github.com/UCTRONICS/U6143_ssd1306.git \
    && mkdir /Addon

COPY /ssd1306/* /Addon/



# COPY run.sh /
# WORKDIR /data
# RUN chmod a+x /run.sh

# #
# CMD [ "/run.sh" ]
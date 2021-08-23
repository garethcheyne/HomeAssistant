ARG BUILD_FROM
FROM $BUILD_FROM
ENV LANG C.UTF-8

RUN set -xe \
    && apk add --no-cache build-base git i2c-tools nano linux-headers cmake \
    && mkdir /UCTronics_OLED

# Copy over the C project
COPY /ssd1306/* /UCTronics_OLED/

COPY run.sh /
WORKDIR /data
RUN chmod a+x /run.sh
CMD [ "/run.sh" ]
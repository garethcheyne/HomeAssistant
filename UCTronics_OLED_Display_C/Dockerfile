ARG BUILD_FROM
FROM $BUILD_FROM
ENV LANG C.UTF-8

RUN set -xe \
    && apk add --no-cache gcc build-base git i2c-tools nano linux-headers cmake pacman

# Copy over the C project
COPY /ssd1306/* /UCTronics_OLED/

COPY run.sh /
COPY start.sh /
WORKDIR /data
RUN chmod a+x /run.sh
RUN chmod a+x /start.sh

CMD [ "/start.sh" ]
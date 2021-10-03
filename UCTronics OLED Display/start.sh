#!/usr/bin/env bashio
set -e

bashio::log.info "Starting UCTronics OLED App...

TEMP_UNIT = $(bashio::config 'temperature_unit')
AUTO_START = $(bashio::config 'stop_auto_run')

echo "Temp Unit \"${TEMP_UNIT}\";"
echo "Temp Unit \"${AUTO_START}\";"
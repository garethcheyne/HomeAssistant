#!/usr/bin/env bashio
set -e

CONFIG_PATH=/data/options.json

TEMP_UNIT="$(bashio::config 'Temperature_Unit')"
DISABLE_AUTO_START="$(bashio::config 'Stop_Auto_Run')"
bashio::log.info "Starting UCTronics OLED App..."
bashio::log.info "Disable Auto Start = ${DISABLE_AUTO_START}"

if [ "$DISABLE_AUTO_START" = false ]; then
    cd /UCTronics_OLED_Python/
    python3 display.py

else
    bashio::log.info "No Auto Run"
    sleep 99999;
fi
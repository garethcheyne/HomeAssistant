#!/usr/bin/env bashio
set -e

CONFIG_PATH=/data/options.json

TEMP_UNIT="$(bashio::config 'temperature_unit')"
DISABLE_AUTO_START="$(bashio::config 'stop_auto_run')"

bashio::log.info "Starting UCTronics OLED App..."
bashio::log.info "Tempature Unit = ${TEMP_UNIT}"
bashio::log.info "Disable Auto Start = ${DISABLE_AUTO_START}"

if [ "$DISABLE_AUTO_START" = false ]; then


    if ls /dev/i2c-1; then 
        bashio::log.info "Found i2c access!";
        bashio::log.info "Loading C script for UCTRONICS OLED...";

        cd /UCTronics_OLED/
        make clean
        make 

        bashio::log.info "Setting Tempature Unit $TEMP_UNIT"
        bashio::log.info "UCTRONICS OLED Display should now be showing information?";
        if [ "$TEMP_UNIT" = "C" ]; then
            ./display C
        else
            ./display F
        fi
    else
        bashio::log.info "Attempting to set up i2c access!";
        exec run.sh        
    fi 
else
    bashio::log.info "No Auto Run"
    cd /UCTronics_OLED/
    make clean
    make 
    sleep 99999;
fi
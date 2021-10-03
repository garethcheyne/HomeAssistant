#!/usr/bin/env bashio
set -e

CONFIG_PATH=/data/options.json

TEMP_UNIT="$(bashio::config 'temperature_unit')"
AUTO_START="$(bashio::config 'stop_auto_run')"

bashio::log.info "Starting UCTronics OLED App..."
bashio::log.info "Tempature Unit = ${TEMP_UNIT}"
bashio::log.info "Disable Auto Start = ${DISABLE_AUTO_START}"

if [ "$DISABLE_AUTO_START" = "false" ]; then

    if [ "$TEMP_UNIT" = "C" ]; then
        if ls /dev/i2c-1; then 
            bashio::log.info "Setting Tempature Unit C"
            bashio::log.info "Found i2c access!";
            bashio::log.info "Loading C Script for UCTRONICS OLED...";
            cd /UCTronics_OLED_C/
            make clean
            make 
            bashio::log.info "UCTRONICS OLED Display should now be showing information?";
            ./display
        else
            exec run.sh
        
        fi  
    else
        if ls /dev/i2c-1; then 
            bashio::log.info "Setting Tempature Unit F"
            bashio::log.info "Found i2c access!";
            bashio::log.info "Loading C Script for UCTRONICS OLED...";
            cd /UCTronics_OLED_F/
            make clean
            make 
            ashio::log.info "UCTRONICS OLED Display should now be showing information?";
            ./display
        else
            exec run.sh
        fi
    fi
fi
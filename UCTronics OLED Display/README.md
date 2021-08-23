# UCTRONICS OLED Display

Enables the the OLED display for UCTRONICS Pi 5 Rack Module.

This addon will utilise code from Adam Outler, https://github.com/adamoutler/HassOSConfigurator/tree/main/Pi4EnableI2C to first enable the I2C interface, you will need to reboot twice as per his documentation. \n 
After I2C is enabled then the display will finally show.


## First Step
Disable "Protection Mode", and start the addon, this will allow Adam's script to enable I2C interface. 
MAKE SURE YOU REBOOT TWICE

## Second Step.
Enable protection made, 
Enable I2C using this HassOS I2C Configurator addon.. here Support is provided on the Home Assistant Community forums, here Make Sure You REBOOT TWICE

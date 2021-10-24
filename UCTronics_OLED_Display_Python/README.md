# UCTRONICS OLED Display - Python Version

Enables the the OLED display for UCTRONICS Pi 4 Rack Module.

### NB, This addon will take some time to initially load as it has to build some python libraries. 

This addon will utilise code from Adam Outler, [GitHub adamoutler](https://github.com/adamoutler/HassOSConfigurator/tree/main/Pi4EnableI2C) to first enable the I2C interface, you will need to reboot twice as per his documentation. After I2C is enabled then the display will finally show.

Special thanks to [DC Walter](https://github.com/dcwalter) for his assistance on this project.

This addon includes a splash screen that will show you the current  version of the Core OS, and HA, and will be presented with an astricx if either require an upgrade. You are also able to set the duration of the slide rotation, and what slides you wish to present.


## First Step
1. Disable "Protection mode"
2. Start the addon, this will allow Adam's script to enable I2C interface. 
### MAKE SURE YOU REBOOT TWICE

## Second Step.
1. Enable "Protection mode"
2. Start the addon
3. Check the "Log" and see if there are any errors.
4. Your OLED should be displaying.

## Some Teaser Screenshots.
### Splash Screen
![Splash Screen](https://github.com/garethcheyne/HomeAssistant/raw/main/UCTronics_OLED_Display_Python/python/img/examples/splash.png?raw=true)
### CPU Stats
![CPU Stats](https://github.com/garethcheyne/HomeAssistant/raw/main/UCTronics_OLED_Display_Python/python/img/examples/cpu.png?raw=true)
### RAM Stats
![RAM Stats](https://github.com/garethcheyne/HomeAssistant/raw/main/UCTronics_OLED_Display_Python/python/img/examples/memory.png?raw=true)
### Storage Stats
![Storage Stats](https://github.com/garethcheyne/HomeAssistant/raw/main/UCTronics_OLED_Display_Python/python/img/examples/storage.png?raw=true)
### Network Stats
![Network Stats](https://github.com/garethcheyne/HomeAssistant/raw/main/UCTronics_OLED_Display_Python/python/img/examples/network.png?raw=true)

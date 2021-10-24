# UCTRONICS OLED Display

### NB This is my first HomeAssistant Add-on so use at own risk

Enables the the OLED display for UCTRONICS Pi 4 Rack Module.

This addon will utilise code from Adam Outler, [GitHub adamoutler](https://github.com/adamoutler/HassOSConfigurator/tree/main/Pi4EnableI2C) to first enable the I2C interface, you will need to reboot twice as per his documentation. After I2C is enabled then the display will finally show.

Special thanks to [DC Walter](https://github.com/dcwalter) for fixing the code to support C unit for temperature, and also fixing CPU usage, and adding the HA Logo.

## First Step
1. Disable "Protection mode"
2. Start the addon, this will allow Adam's script to enable I2C interface. 
### MAKE SURE YOU REBOOT TWICE

## Second Step.
1. Enable "Protection mode"
2. Start the addon
3. Check the "Log" and see if there are any error.
4. Your OLED should be displaying.


# New Python Project (In Development)
This part of the project is still under active development, and yet will not run on HAOS.

## Some Teaser Screenshots.
### Splash Screen
![Splash Screen](https://github.com/garethcheyne/HomeAssistant/raw/main/UCTronics%20OLED%20Display/python/img/examples/splash.png?raw=true)
### CPU Stats
![CPU Stats](https://github.com/garethcheyne/HomeAssistant/raw/main/UCTronics%20OLED%20Display/python/img/examples/cpu.png?raw=true)
### RAM Stats
![RAM Stats](https://github.com/garethcheyne/HomeAssistant/raw/main/UCTronics%20OLED%20Display/python/img/examples/memory.png?raw=true)
### Storage Stats
![Storage Stats](https://github.com/garethcheyne/HomeAssistant/raw/main/UCTronics%20OLED%20Display/python/img/examples/storage.png?raw=true)
### Network Stats
![Network Stats](https://github.com/garethcheyne/HomeAssistant/raw/main/UCTronics%20OLED%20Display/python/img/examples/network.png?raw=true)

## TODO
- [x] Create base line project, and display is standard RasPi OS.
- [x] Get Satistics (CPU, Network, RAM, Storage).
- [x] Create HA Splash Screen.
- [ ] Get RPi.GPIO to work in HA Docker.
- [ ] Pull further satistics from HA API.
- [ ] User Congif, allow users to set duration, and what statistics to show.


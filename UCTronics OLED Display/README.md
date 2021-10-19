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
This part of the project is still under active devlelopment, and yet will not run on HAOS.

## Some Teaser Screenshots.
### Splash Screen
![Splash Screen](python/img/examples/splash.png?raw=true "Splash Screen")
### CPU Stats
![CPU Stats](python/img/examples/cpu.png?raw=true "CPU Stats")
### RAM Stats
![RAM Stats](python/img/examples/memory.png?raw=true "RAM Stats")
### Storage Stats
![Storage Stats](python/img/examples/storage.png?raw=true "Storage Stats")
### Network Stats
![Network Stats](python/img/examples/network.png?raw=true "Network Stats")

## TODO
- [x] Create base line project, and display is standars RasPi OS.
- [x] Get Satistics (CPU, Network, RAM, Storage).
- [x] Create HA Splash Screen
- [ ] Get RPi.GPIO to work in HA Docker
- [ ] Pull further satistics from HA API.


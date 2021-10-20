# SPDX-FileCopyrightText: 2017 Tony DiCola for Adafruit Industries
# SPDX-FileCopyrightText: 2017 James DeVito for Adafruit Industries
# SPDX-License-Identifier: MIT

## REF https://pillow.readthedocs.io/
## REF Icons, 

# This example is for use on (Linux) computers that are using CPython with
# Adafruit Blinka to support CircuitPython libraries. CircuitPython does
# not support PIL/pillow (python imaging library)!
import math
from os import stat
import time
import sys, getopt
import subprocess
import requests

from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont, ImageOps
import adafruit_ssd1306

# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)
# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# Clear display.
disp.fill(0)
disp.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.

width = disp.width
height = disp.height

image = Image.new("1", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)


# Load default font.
# font = ImageFont.load_default()
p = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 9)
p_bold = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 9)
small = ImageFont.truetype("usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 8)
smaller = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 7)


img_network = Image.open(r"./img/ip-network.png") 
img_mem = Image.open(r"./img/database.png") 
#img_disk = Image.open(r"./img/harddisk.png") 
img_disk = Image.open(r"./img/database-outline.png") 
img_ha_logo = m = Image.open(r"./img/home-assistant-logo.png") 
img_cpu_64 = Image.open(r"./img/cpu-64-bit.png") 


# Move left to right keeping track of the current x position for drawing shapes.
x = 0

def start():
    while True:        
        show_splash(5)
        show_network(5)
        show_storage(5)
        show_memory(5)
        show_cpu_temp(5, 'c')

def show_storage(duration):
    storage =  shell_cmd('df -h | awk \'$NF=="/"{printf "%d,%d,%s", $3,$2,$5}\'')

    storage = storage.split(',')

    # Clear Canvas
    draw.rectangle((0,0,128,32), outline=0, fill=0)

    # Resize and merge icon to Canvas
    icon = img_disk.resize([32,32])  
    image.paste(icon,(0,0))

    draw.text((36, 0), "USED: " + storage[0] + ' GB \n', font=p, fill=255)
    draw.text((36, 11), "TOTAL: " + storage[1] + ' GB \n', font=p, fill=255)
    draw.text((36, 21), "UTILIZED: " + storage[2] + ' \n', font=p, fill=255) 

    image.save(r"./img/examples/storage.png")    

    disp.image(image)
    disp.show()
    time.sleep(duration)  

def show_memory(duration):

    mem =  shell_cmd("free -m | awk 'NR==2{printf \"%.1f,%.1f,%.0f%%\", $3/1000,$2/1000,$3*100/$2 }'")
    mem = mem.split(',')

    # Clear Canvas
    draw.rectangle((0,0,128,32), outline=0, fill=0)

    # Resize and merge icon to Canvas
    icon = img_mem.resize([32,32])  
    image.paste(icon,(0,0))

    draw.text((36, 0), "USED: " + mem[0] + ' GB \n', font=p, fill=255)
    draw.text((36, 11), "TOTAL: " + mem[1] + ' GB \n', font=p, fill=255)
    draw.text((36, 21), "UTILIZED: " + mem[2] + ' \n', font=p, fill=255)  

    image.save(r"./img/examples/memory.png")   

    disp.image(image)
    disp.show()
    time.sleep(duration) 


def show_cpu_temp(duration, unit):

    cpu = shell_cmd("top -bn1 | grep load | awk '{printf \"%.2f\", $(NF-2)}'")
    temp =  float(shell_cmd("cat /sys/class/thermal/thermal_zone0/temp")) / 1000.00
    uptime = shell_cmd("uptime -p")

    # Check temapture unit and convert if required.
    if (unit == 'c'): 
        temp = "%0.2f °C " % (temp)
    else:
        temp = "%0.2f °F " % (temp * 9.0 / 5.0 + 32)


    # Clear Canvas
    draw.rectangle((0,0,128,32), outline=0, fill=0)

    # Resize and merge icon to Canvas
    icon = img_cpu_64.resize([26,26])  
    image.paste(icon,(-2,3))

    draw.text((29, 0), 'TEMP: ' + temp, font=p, fill=255)
    draw.text((29, 11), 'LOAD: '+ cpu + "% ", font=p, fill=255)  
    draw.text((29, 21), uptime.upper(), font=small, fill=255)

    image.save(r"./img/examples/cpu.png")

    disp.show()
    time.sleep(duration)


def show_network(duration):
    hostname = shell_cmd("hostname")
    ip4 = shell_cmd("hostname -I | cut -d' ' -f1")
    mac = shell_cmd("cat /sys/class/net/eth0/address")

    # Clear Canvas
    draw.rectangle((0,0,128,32), outline=0, fill=0)

    # Resize and merge icon to Canvas
    icon = img_network.resize([26,26])  
    image.paste(icon,(-2,3))

    draw.text((29, 0), "HOST " + hostname.upper(), font=small, fill=255)
    draw.text((29, 11), "IP4 " + ip4, font=small, fill=255)    
    draw.text((29, 21), "MAC " + mac.upper(), font=small, fill=255)    

    image.save(r"./img/examples/network.png")

    disp.image(image)
    disp.show()
    time.sleep(duration)


def get_ha_info():

    url = "http://192.168.0.210:8123/api/config"
    headers = ""
    response = requests.get(url)   
    print(response.json()) 

def get_text_center(text, font, center_point):
    w, h = draw.textsize(text, font=font)

    return (center_point -(w/2))


def show_splash(duration):

    # Draw a padded black filled box with style.border width.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    # Get HA Logo and Resize
    logo = img_ha_logo.resize([32,32])
    logo = ImageOps.invert(logo)  
    
    # Merge HA Logo with Canvas.
    image.paste(logo,(-2,0))

    draw.line([(34, 16),(123,16)], fill=255, width=1)

    ln1 = "Home Assistant"
    ln1_x = get_text_center(ln1, p_bold, 78)
    draw.text((ln1_x, 4), ln1, font=p_bold, fill=255)

    # Write Test, Eventually will get from HA API.
    ln2 = "OS 6.5 - 2021.10.6"
    ln2_x = get_text_center(ln2, small, 78)
    draw.text((ln2_x, 20), ln2, font=small, fill=255)

    # Display Image to OLED
    image.save(r"./img/examples/splash.png")
    disp.image(image)
    disp.show() 
    time.sleep(duration)
  

def get_status():
    stats = {
        'ip4': shell_cmd("hostname -I | cut -d' ' -f1"),
        'mac': shell_cmd("cat /sys/class/net/eth0/address"),
        'cpu': shell_cmd("top -bn1 | grep load | awk '{printf \"%.2f\", $(NF-2)}'"),
        'dsk': shell_cmd('df -h | awk \'$NF=="/"{printf "%d,%d,%s", $3,$2,$5}\''),
        'mem': shell_cmd("free -m | awk 'NR==2{printf \"%.1f,%.1f,%.0f%%\", $3/1000,$2/1000,$3*100/$2 }'"),
        'temp': float(shell_cmd("cat /sys/class/thermal/thermal_zone0/temp")) / 1000.00 
        }    

    print(stats) 
    return stats

def shell_cmd(cmd):
    return subprocess.check_output(cmd, shell=True).decode("utf-8")

if __name__ == "__main__":
    print(str(sys.argv))
    start()
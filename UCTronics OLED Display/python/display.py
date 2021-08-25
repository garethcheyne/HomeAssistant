# SPDX-FileCopyrightText: 2017 Tony DiCola for Adafruit Industries
# SPDX-FileCopyrightText: 2017 James DeVito for Adafruit Industries
# SPDX-License-Identifier: MIT

# This example is for use on (Linux) computers that are using CPython with
# Adafruit Blinka to support CircuitPython libraries. CircuitPython does
# not support PIL/pillow (python imaging library)!
import math
import time
import subprocess

from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
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
p = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 8)
h1_bold = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

def load():
    logo()
    info()

def logo():

    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    draw.text((0, 5), "Home Assitant", font=h1_bold, fill=255)
    disp.image(image)
    disp.show() 
    time.sleep(10)
    

def info():
    while True:
        # Draw a black filled box to clear the image.
        draw.rectangle((0, 0, width, height), outline=0, fill=0)

        # Shell scripts for system monitoring from here:
        # https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load

        stats = get_status()

        # Write four lines of text.
        draw.text((x, top + 0), "IP: " + stats['ip4'], font=p, fill=255)
        draw.text((x, top + 8), stats['cpu'], font=p, fill=255)
        draw.text((x, top + 16), stats['mem'], font=p, fill=255)
        draw.text((x, top + 25), stats['dsk'], font=p, fill=255)

        # Display image.
        disp.image(image)
        disp.show()
        time.sleep(0.1)


def get_status():
    stats = {
        'ip4': shell_cmd("hostname -I | cut -d' ' -f1"),
        'cpu': shell_cmd("top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"),
        'dsk': shell_cmd('df -h | awk \'$NF=="/"{printf "Disk: %d/%d GB  %s", $3,$2,$5}\''),
        'mem': shell_cmd("free -m | awk 'NR==2{printf \"Mem: %s/%s MB  %.2f%%\", $3,$2,$3*100/$2 }'")
        }            
    return stats

def shell_cmd(cmd):
    return subprocess.check_output(cmd, shell=True).decode("utf-8")

if __name__ == "__main__":
    load()
/******
Demo for ssd1306 i2c driver for  Raspberry Pi 
******/
#include <stdio.h>
#include "ssd1306_i2c.h"
#include "time.h"
#include <unistd.h>
#include <string.h>

int main(int argc, char *argv[])
{
  unsigned char symbol = 0;
  ssd1306_begin(SSD1306_SWITCHCAPVCC, SSD1306_I2C_ADDRESS); // LCD Screen initialization
  if (i2cd < 0)
  {
    printf("I2C device failed to open\r\n");
    return 0;
  }
  usleep(150 * 1000);  // Short delay Ensure the normal response of the lower function
  FirstGetIpAddress(); // Get IP address

  unsigned char temp_unit = 'C';
  if (argc > 1 && (strcmp(argv[1], "f") == 0 || strcmp(argv[1], "F") == 0)) 
  {
  
  }
  while (1) 
  {
    LCD_Display(symbol, temp_unit);
    sleep(3);
    symbol = ++symbol % 4;
  }
  return 0;
}

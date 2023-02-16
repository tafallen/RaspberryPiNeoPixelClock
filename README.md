# Raspberry Pi (and Pico) NeoPixel Clock

## Project Aims

1. To build the project myself without using anyone else's code other than the NeoPixel libraries (and the Pico Plasma2040W example wifi code)
2. To make the clock flicker as little as possible when updating
3. To make the clock as configurable as possible in terms of number of pixels and colours used
4. To make the electronics fit in an Altoids tin

## Kit List

For the Pi based clock:
* Raspberry Pi (internet connected) - I'm using a Raspberry Pi Zero W
* USB C breakout board
* USB Micro Power Supply - For the Raspberry Pi

For the Pico based clock:
* Pimoroni Plasma2040 or Pimoroni Plasma2040W

For both:
* USB C Power Supply - Needs enough ampage to drive the ring
* Some wires for connecting things
* Soldering gear

## (Very) Brief Build Instructions

For the Raspberry Pi Clock:
1. Solder a wire to the Ground and VBus on the USB C Breakout Board
2. Solder the USB C VBus wire to the +5v connector on the AdaFruit NeoPixel ring
3. Solder the USB C Ground wire to the GND connector on the AdaFruit NeoPixel ring
4. Solder a wire to the Data In connector of the AdaFruit NeoPixel ring
5. Connect the Data In connector to Pin 18 of the Pi 
6. Power up the Pi and also connect the power to the USB C breakout

Nothing should light up on the NeoPixel ring. If you do get lights turning on then you've probably got an underpowered USB C or Pi power supply. I did at one point and it made me very confused!

For the Pico Plasma 2040 based clock:
1. Solder the USB C VBus wire to the +5v connector on the AdaFruit NeoPixel ring and connect the other end to the Plasma 5V terminal
2. Solder the USB C Ground wire to the GND connector on the AdaFruit NeoPixel ring and connect the other end to the - terminal on the Plasma
3. Solder a wire to the Data In connector of the AdaFruit NeoPixel ring and connect the other end to the Plasma's DA terminal 

For the Pico Plasma 2040W based clock:
1. Solder the USB C VBus wire to the +5v connector on the AdaFruit NeoPixel ring and connect the other end to the Plasma 5V terminal
2. Solder the USB C Ground wire to the GND connector on the AdaFruit NeoPixel ring and connect the other end to the - terminal on the Plasma
3. Solder a wire to the Data In connector of the AdaFruit NeoPixel ring and connect the other end to the Plasma's Pixels terminal 


## Install Python bits and bobs

For the Raspberry Pi clock:
1. Check your Pi is up to date by doing a `sudo apt-get update` and a `sudo apt-get upgrade`
2. Install the required NeoPixel libraries as detailed here: https://learn.adafruit.com/neopixels-on-raspberry-pi/python-usage
3. Clone this git repo to your Pi
4. Go into the Pi folder `cd Pi`
5. Run the command `sudo Python3 clock.py`

For the Pico Plasma 2040(W) based clock:
1. Download the code
2. Rename the file as main.py
3. Copy main.py to your plasma's root folder
4. If it's a Plasma2040W: Configure the wifi settings on your Pico Plasma2040W
5. Restart the Plsma2040

The clock should be running now. if it's a Plasma2040W and the WiFi settings give access to the internet then the time should also be correct!

## Status

Thus far I've achieved aims #1, #2 and #4 but I'm still working on #3. It's all a but minimal and hacky at this point but then again I'm not a professional Python programmer!

I've just updated all this to support the new Plasma2040W. This enables a direct connection to the internet and an automatic sync to an NTP server so no need to manually set the time!

import plasma
import time
from plasma import plasma2040
from pimoroni import RGBLED, Button

num_leds = 24
sstep = 60/num_leds
mstep = 60/num_leds
hstep = 12/num_leds

last_second = 0
last_minute = 0
last_hour = 0

button_a = Button(plasma2040.BUTTON_A)
button_b = Button(plasma2040.BUTTON_B)

led_strip = plasma.WS2812(num_leds, 0, 0, plasma2040.DAT)
led_strip.start()

while True:
    new_second = (last_second+1)%60
    new_minute = last_minute
    new_hour = last_hour

    if button_a.read():
        new_hour = (new_hour+1)%12

    if button_b.read():
        new_minute = (new_minute+1)%60
        
    if last_minute >= 59 and last_second >= 59:
        new_hour = (new_hour+1)%12

    if last_second >= 59:
        new_minute = (new_minute+1)%60

    led_strip.set_rgb(int(last_second/sstep), 0, 0, 0)
    led_strip.set_rgb(int(last_minute/mstep), 0, 0, 0)
    led_strip.set_rgb(int(last_hour/hstep), 0, 0, 0)
    led_strip.set_rgb(int(new_second/sstep), 10, 10, 0)
    led_strip.set_rgb(int(new_minute/mstep), 10, 0, 10)
    led_strip.set_rgb(int(new_hour/hstep), 0, 10, 10)

    last_second = new_second
    last_minute = new_minute
    last_hour = new_hour
    time.sleep(1)

import ntptime
import WIFI_CONFIG
from network_manager import NetworkManager
import uasyncio
import time
import plasma
from plasma import plasma_stick
from machine import Pin

num_leds = 24
sstep = 60/num_leds
mstep = 60/num_leds
hstep = 12/num_leds

last_second = 0
last_minute = 0
last_hour = 0

def spooky_rainbows():
    print('SPOOKY RAINBOWS!')
    HUE_START = 30  # orange
    HUE_END = 140  # green
    SPEED = 0.3  # bigger = faster (harder, stronger)

    distance = 0.0
    direction = SPEED
    while True:
        for i in range(NUM_LEDS):
            # generate a triangle wave that moves up and down the LEDs
            j = max(0, 1 - abs(distance - i) / (NUM_LEDS / 3))
            hue = HUE_START + j * (HUE_END - HUE_START)

            led_strip.set_hsv(i, hue / 360, 1.0, 0.8)

        # reverse direction at the end of colour segment to avoid an abrupt change
        distance += direction
        if distance > NUM_LEDS:
            direction = - SPEED
        if distance < 0:
            direction = SPEED

        time.sleep(0.01)
        
def status_handler(mode, status, ip):
    # reports wifi connection status
    print(mode, status, ip)
    print('Connecting to wifi...')
    # flash while connecting
    for i in range(num_leds):
        led_strip.set_rgb(i, 255, 255, 255)
        time.sleep(0.02)
    for i in range(num_leds):
        led_strip.set_rgb(i, 0, 0, 0)
    if status is not None:
        if status:
            print('Wifi connection successful!')
        else:
            print('Wifi connection failed!')
            
def clearPreviousTime():
    led_strip.set_rgb(int(last_second/sstep), 0, 0, 0)
    led_strip.set_rgb(int(last_minute/mstep), 0, 0, 0)
    led_strip.set_rgb(int(last_hour/hstep), 0, 0, 0)

pico_led = Pin('LED', Pin.OUT)
led_strip = plasma.WS2812(num_leds, 0, 0, plasma_stick.DAT, color_order=plasma.COLOR_ORDER_RGB)
led_strip.start()

# set up wifi
try:
    network_manager = NetworkManager(WIFI_CONFIG.COUNTRY, status_handler=status_handler)
    uasyncio.get_event_loop().run_until_complete(network_manager.client(WIFI_CONFIG.SSID, WIFI_CONFIG.PSK))
    ntptime.settime()
except Exception as e:
    print(f'Wifi connection failed! {e}')
    # if no wifi, then you get...
    spooky_rainbows()

while True:
    t = time.localtime()
    
    new_second = t[5]
    new_minute = t[4]
    new_hour = t[3] % 12

    clearPreviousTime()
    
    s = int(new_second/sstep)
    m = int(new_minute/mstep)
    h = int(new_hour/hstep)
    
    if s==m and m == h:
        led_strip.set_rgb(s, 155, 155, 155)
    elif s==m:
        led_strip.set_rgb(s, 155, 0, 155)
        led_strip.set_rgb(h, 0, 155, 0)
    elif m == h:
        led_strip.set_rgb(s, 155, 0, 0)
        led_strip.set_rgb(m, 0, 155, 155)
    elif s == h:
        led_strip.set_rgb(s, 155, 155, 0)
        led_strip.set_rgb(m, 0, 0, 155)
    else:
        led_strip.set_rgb(s, 155, 0, 0)
        led_strip.set_rgb(m, 0, 0, 155)
        led_strip.set_rgb(h, 0, 155, 0)

    last_second = new_second
    last_minute = new_minute
    last_hour = new_hour

    time.sleep(0.5)

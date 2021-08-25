import board
import time
import neopixel
import math

# setup the pixels
pixels = neopixel.NeoPixel(board.D18, 24)

# clear the ring
pixels.fill((0,0,0))

hour = 0
minute = 0
second = 0

last_second = 0
last_minute = 0
last_hour = 0

# while forever
while True:
  # Update seconds
  last_second = second
  second += 1

  # Update minutes
  if second > 59:
    minute += 1

  # Update hours
  if minute > 59:
    hour += 1

  second = second % 60
  minute = minute % 60
  hour = hour % 12

  # Update Ring
  s = math.floor(second/(60/24))
  m = math.floor(minute/(60/24))
  h = math.floor((hour % 12)*2)
  
  pixels[last_second] = (0,0,0)
  pixels[last_minute] = (0,0,0)
  pixels[last_hour] = (0,0,0)
  
  last_second = s
  last_minute = m
  last_hour = h
  
  pixels[s] = (10,0,0)
  pixels[m] = (10,10,0)
  pixels[h] = (0,10,10)

  time.sleep(1)
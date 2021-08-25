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

# while forever
while True:
  # Update seconds
  second = ( second + 1 ) % 60
  # Update minutes

  # Update hours

  # Update Ring
  s = math.floor(second/(60/24))
  pixels[s] = (10,0,0)
  time.sleep(1)
#   # get the date time
#   t = datetime.datetime.now().time()
#   h = math.floor((t.hour % 12)*2)
#   m = math.floor(t.minute/(60/24))
#   s = math.floor(t.second/(60/24))

#   # if the seconds position has changed
#   if last_second != s :
#     # if the second was on the hour or minute then don't update else...
#     if last_second != h and last_second != m:
#       pixels[last_second] = (0,0,0)
#     last_second = s
#     pixels[last_second] = (10,10,0)

#   # if the minutes position has changed or
#   # the seconds position has wiped out the minutes
#   if last_minute != m or last_minute == last_second:
#     # if the minute was on the hour then don't update else...
#     if last_minute != h:
#       pixels[last_minute] = (0,0,0)
#     last_minute = m
#     pixels[last_minute] = (10,0,10)

#   # if the hour position has changed or
#   # the seconds or minutes position has wiped out the hour
#   if last_hour != h or last_hour == last_second or last_hour == last_minute:
#     pixels[last_hour] = (0,0,0)
#     last_hour = h
#     pixels[last_hour] = (0,0,10)

#   # sleep for 2/5ths of a second so we update a little more than twice a second
#   time.sleep(0.4)
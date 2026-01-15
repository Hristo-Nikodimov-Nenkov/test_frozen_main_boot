from machine import Pin
from neopixel import NeoPixel
from uasyncio import sleep_ms, run

rgb_led = NeoPixel(Pin(23), 1)

colors = [(255,0,0),(0,255,0),(0,0,255),(0,0,0)]

async def start():
    while True:
        for c in colors:
            rgb_led[0] = c
            rgb_led.write()
            await sleep_ms(250)

run(start())
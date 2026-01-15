from machine import Pin
from utime import sleep

board_led = Pin(25, Pin.OUT)
for _ in range(10):
    board_led.toggle()
    sleep(0.25)
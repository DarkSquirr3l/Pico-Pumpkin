import machine
import utime

# identify button locations
green_button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
yellow_button = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)

# identify led location
green_led = machine.Pin(16, machine.Pin.OUT)

while True:
    green_led.value(1)
    utime.sleep(2)
    green_led.value(0)
    utime.sleep(2)
    
import machine
import utime
import _thread

# Button and LED pins
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
all_leds = [machine.Pin(pin, machine.Pin.OUT) for pin in [16, 17, 18, 19, 20, 21, 22, 26, 27, 28]]
yel_leds = [machine.Pin(pin, machine.Pin.OUT) for pin in [16, 17, 18, 19, 20]]
red_leds = [machine.Pin(pin, machine.Pin.OUT) for pin in [21, 22, 26, 27, 28]]


# Global button state
button_pressed = False

# Button reader thread
def button_reader_thread():
    global button_pressed
    while True:
        if button.value() == 1:
            button_pressed = True
        utime.sleep(0.01)

_thread.start_new_thread(button_reader_thread, ())

def led_on(leds):
    for led in leds:
        led.value(1)

def led_off(leds):
    for led in leds:
        led.value(0)

# All leds of to start
led_off(all_leds)

# Main loop
i = 1
while True:
    print (i)
    if button_pressed:
        i += 1
        if i > 3:
            i = 1
        button_pressed = False

    if i < 3:
        for j in range (10):
            led_on(red_leds)
            led_off(yel_leds)
            utime.sleep(0.2 if i == 2 else 0.5)

            led_off(red_leds)
            led_on(yel_leds)
            utime.sleep(0.2 if i == 2 else 0.5)
        
    if i == 2:
        for k in range (20):
            led_on(red_leds)
            led_off(yel_leds)
            utime.sleep(0.05)

            led_off(red_leds)
            led_on(yel_leds)
            utime.sleep(0.05)

    if i == 3: # need re working.
        for led in all_leds[:2]:
            led.value(1)
        utime.sleep(0.2)

        for led in all_leds[:2]:
            led.value(0)
        utime.sleep(0.2)

        for led in all_leds[:2]:
            led.value(1)
        utime.sleep(0.2)

        for led in all_leds[5:]:
            led.value(0)
        utime.sleep(0.2)
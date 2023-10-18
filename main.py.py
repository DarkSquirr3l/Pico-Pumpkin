import machine
import utime
import _thread

# identify button location
green_button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

# global button definition
global button_pressed
button_pressed = False

# identify led location
yel_1_led = machine.Pin(16, machine.Pin.OUT)
yel_2_led = machine.Pin(17, machine.Pin.OUT)
yel_3_led = machine.Pin(18, machine.Pin.OUT)
yel_4_led = machine.Pin(19, machine.Pin.OUT)
yel_5_led = machine.Pin(20, machine.Pin.OUT)
red_1_led = machine.Pin(21, machine.Pin.OUT)
red_2_led = machine.Pin(22, machine.Pin.OUT)
red_3_led = machine.Pin(26, machine.Pin.OUT)
red_4_led = machine.Pin(27, machine.Pin.OUT)
red_5_led = machine.Pin(28, machine.Pin.OUT)

def button_reader_thread():
    global button_pressed
    while True:
        if green_button.value() == 1:
            button_pressed = True
        utime.sleep(0.01)
        
_thread.start_new_thread(button_reader_thread, ())

i = 1
while True:
    
    if button_pressed == True:
        i += 1
        if i > 3:
            i = 1
        button_pressed = False
    
    if i == 1:
        yel_1_led.value(1)
        yel_2_led.value(1)
        yel_3_led.value(1)
        yel_4_led.value(1)
        yel_5_led.value(1)
        utime.sleep(1)
        yel_1_led.value(0)
        yel_2_led.value(0)
        yel_3_led.value(0)
        yel_4_led.value(0)
        yel_5_led.value(0)
        red_1_led.value(1)
        red_2_led.value(1)
        red_3_led.value(1)
        red_4_led.value(1)
        red_5_led.value(1)
        utime.sleep(1)
        red_1_led.value(0)
        red_2_led.value(0)
        red_3_led.value(0)
        red_4_led.value(0)
        red_5_led.value(0)
    elif i == 2:
        for j in range (10):
            yel_1_led.value(1)
            yel_2_led.value(1)
            yel_3_led.value(1)
            yel_4_led.value(1)
            yel_5_led.value(1)
            utime.sleep(0.2)
            yel_1_led.value(0)
            yel_2_led.value(0)
            yel_3_led.value(0)
            yel_4_led.value(0)
            yel_5_led.value(0)
            red_1_led.value(1)
            red_2_led.value(1)
            red_3_led.value(1)
            red_4_led.value(1)
            red_5_led.value(1)
            utime.sleep(0.2)
            red_1_led.value(0)
            red_2_led.value(0)
            red_3_led.value(0)
            red_4_led.value(0)
            red_5_led.value(0)
        for k in range (20):
            yel_1_led.value(1)
            yel_2_led.value(1)
            yel_3_led.value(1)
            yel_4_led.value(1)
            yel_5_led.value(1)
            utime.sleep(0.05)
            yel_1_led.value(0)
            yel_2_led.value(0)
            yel_3_led.value(0)
            yel_4_led.value(0)
            yel_5_led.value(0)
            red_1_led.value(1)
            red_2_led.value(1)
            red_3_led.value(1)
            red_4_led.value(1)
            red_5_led.value(1)
            utime.sleep(0.05)
            red_1_led.value(0)
            red_2_led.value(0)
            red_3_led.value(0)
            red_4_led.value(0)
            red_5_led.value(0)
    else:
        yel_1_led.value(1)
        yel_2_led.value(1)
        yel_3_led.value(1)
        yel_4_led.value(1)
        yel_5_led.value(1)
        red_1_led.value(1)
        red_2_led.value(1)
        red_3_led.value(1)
        red_4_led.value(1)
        red_5_led.value(1)
        utime.sleep(0.2)
        yel_1_led.value(0)
        yel_2_led.value(0)
        utime.sleep(0.2)
        red_1_led.value(0)
        red_2_led.value(0)
        yel_1_led.value(1)
        yel_2_led.value(1)
        utime.sleep(0.2)
        red_1_led.value(1)
        red_2_led.value(1)
        red_3_led.value(0)
        red_4_led.value(0)
        red_5_led.value(0)
        utime.sleep(0.2)
        yel_1_led.value(1)
        yel_2_led.value(1)
        yel_3_led.value(0)
        yel_4_led.value(0)
        yel_5_led.value(0)
        utime.sleep(0.2)
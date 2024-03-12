# Filename: pico_w_onboard_led.py
import time
def onboard_led_blink():
    led = machine.Pin('LED', machine.Pin.OUT)
    led.on()
    time.sleep(.5)
    led.off()
    time.sleep(.5)
while True:
    onboard_led_blink()

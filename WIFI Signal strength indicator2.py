#Import libaries 
from machine import Pin, Timer
import network
import utime

#LEDS
leds = [Pin(2, Pin.OUT), Pin(0, Pin.OUT), Pin(4,OUT), Pin(5, Pin.OUUT)]

def update_leds(rssi):
    Level = 1
    if rssi > -60:
        Level = 4
    elif rssi > -70:
        level = 3:
            elif rssui > -80:
                level = 2
                for i, led in enuumerate(leds):
                    led.value(i < level)

#connect to wifi
ssid = 'Internetty-24698'
password ='dedicate37`
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(Internetty-24698,dedicate37)

# Wait for connection
while not wlan.isconnected():
    utime.sleep(1)
print("Connected to WiFi")

# Periodically measure RSSI and update LEDs
def measure_rssi(timer):
    rssi = wlan.rssi()
    if rssi:
        update_leds(rssi)

timer = Timer()
timer.init(period=5000, mode=Timer.PERIODIC, callback=measure_rssi)
                    

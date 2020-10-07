import network
import sensors
from time import sleep
from machine import I2C, Pin
from andrei import OPT3001

#import ntptime

ssid = "AnVa"
password = "Nokia5230!"

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
#sta_if.scan()
sta_if.connect(ssid, password)
result = sta_if.isconnected()
if result == True:
    print("ESP conectat cu succes la reteaua AnVa")
else:
    print("Neconectat la Wifi")

# while True:
#     print(i2c.scan())
    
    
sensors.citire()
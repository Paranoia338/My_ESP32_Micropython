from machine import I2C, Pin
from time import sleep

class OPT3001(object):
    def __init__(self, bus, address):
        self.bus = bus
        self.address = address
        self.data = bytearray(2)
        self.config_reg = 1
        self.result_reg = 0
#         bus = I2C(scl=Pin(13), sda=Pin(15), freq=400000)
#         address = 70
    def config(self):
        self.bus.writeto_mem(self.address, self.config_reg, b'\xCE10')
        sleep(0.1)
    def roler(self):
        self.bus.writeto_mem(self.address, self.config_reg, b'\x00')
        sleep(0.1)
        self.bus.readfrom_mem_into(self.address, self.result_reg, self.data)
        value = (self.data[0] << 8) | self.data[1]
        raw_data = value
        mantisa = raw_data & 0xFFF
        exponent = (raw_data & 0xF000) >> 12
        luminozitate = mantisa * (0.01 * pow(2, exponent))
#         print(luminozitate)
#         sleep(1)
        return luminozitate


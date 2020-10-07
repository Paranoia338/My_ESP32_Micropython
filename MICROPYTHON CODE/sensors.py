from bmp180 import BMP180
from machine import I2C, Pin, ADC
from time import sleep
from andrei import OPT3001
import dht, tony

sensor = dht.DHT22(Pin(12))

bus1 =  I2C(scl=Pin(22), sda=Pin(23), freq=100000)   # on esp32
bmp180 = BMP180(bus1)
bmp180.oversample_sett = 2
bmp180.baseline = 101325

a = '\u00b0'

mq135 = tony.MQ135(Pin(32))

bus = I2C(scl=Pin(13), sda=Pin(15), freq=400000)
address = 70
obiect = OPT3001(bus, address)
obiect.config()

# umid_sol = ADC(Pin(26))
# valoare = umid_sol.read()

def citire():
    while True:
      try:
        sleep(1)
        sensor.measure()
        temp1 = sensor.temperature()
        hum = sensor.humidity()
    #    temp_f = temp1 * (9/5) + 32.0
        sleep(2)
        temp2 = bmp180.temperature
        p = bmp180.pressure
        p_in_mb = p/100
        p_in_hg = p_in_mb*0.02953
        altitude = bmp180.altitude
        rzero = mq135.get_rzero()
        corrected_rzero = mq135.get_corrected_rzero(temp1, hum)
        resistance = mq135.get_resistance()
        ppm = mq135.get_ppm()
        corrected_ppm = mq135.get_corrected_ppm(temp1, hum)
        
        lux = obiect.roler()
        
        umid_sol = ADC(Pin(33))
        valoare = umid_sol.read()
                
        print('\nTemperatura_DHT_22: {:.2f}{}C'.format(temp1, a))
        print("Temperatura_BMP_180: {:.2f}{}C".format(temp2, a))
        print('Umiditatea: %3.1f %%' %hum)
        print("Presiune: {} milibari.\tPresiune: {} coloana de mercur.".format(p_in_mb, p_in_hg))
        print("Altitudine: {:.2f} m".format(altitude))
        print("Concentratie CO2: {} ppm".format(corrected_ppm))
        print("Luminozitate: {}".format(lux))
        print("Umiditate sol: {}".format(valoare))
        
      except OSError as e:
        print('Failed to read sensor.')

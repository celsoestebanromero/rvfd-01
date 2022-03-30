from machine import Pin,ADC
from time import  sleep
from math import log

adc = ADC(26)

R1= 10000
BETA= 3950
while True:
  lect = adc.read_u16()
  print("Valor del ADC es:{}".format(lect))
  tension = 3.3 / 65535 * lect 
  print("valor de tension es: {}".format(tension))
  sleep(1)
  R2= (tension*R1)/(3.3-tension)
  print("Valor de R2 es: {}".format(R2))
  temperatura = (BETA / (log(R2/R1) + BETA / 298)) - 273
  print("Valor de Temperatura es:{}".format(temperatura))
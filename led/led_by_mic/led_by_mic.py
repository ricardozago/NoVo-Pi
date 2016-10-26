import wiringpi
from smbus import SMBus
from time import sleep

#Need sudo permission for using wiringpi

def setup():

    wiringpi.wiringPiSetupGpio()
    wiringpi.wiringPiI2CSetup(0x90>>1)		
    for gpio in gpio_list:	
        wiringpi.pinMode(gpio,1) #output pins
		
def led_n(delay = 0.5,n = 0):
	
    for i in range(n):
       wiringpi.digitalWrite(gpio_list[i],1)
    for i in range(n,len(gpio_list)):	    	
       wiringpi.digitalWrite(gpio_list[i],0)
			

# Pins used to make the 'V' shaped LEDs blink
gpio_list = [17, 27, 22 , 5, 6, 13 , 26] 

bus = SMBus(0)

Ain0 = 0x00
Samples = 20
setup()

while 1:

    inputMax = 0
    inputMin = 255
    fd = 0
    value = list()
    wiringpi.wiringPiI2CWrite(fd,0x40 | Ain0)

    value.append(wiringpi.wiringPiI2CRead(fd))
    for i in range(Samples):
	value.append(wiringpi.wiringPiI2CRead(fd));
	inputMin = min(inputMin, value[i]);
    	inputMax = max(inputMax, value[i]);

    print value	
    diff = (inputMax - inputMin)
    blink = diff/8
    led_n(blink)
	



    













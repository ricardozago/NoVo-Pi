import wiringpi
from smbus import SMBus
from time import sleep

#Need sudo permission for using wiringpi

def setup():

    wiringpi.wiringPiSetupGpio()		
    for gpio in gpio_list:	
        wiringpi.pinMode(gpio,1) #output pins
		
def led_n(n = 0):
    if n > len(gpio_list):
	n = len(gpio_list)
    if n < 0:
	n = 0
    for i in range(n):
       wiringpi.digitalWrite(gpio_list[i],1)
    for i in range(n,len(gpio_list)):	    	
       wiringpi.digitalWrite(gpio_list[i],0)
			

# Pins used to make the 'V' shaped LEDs blink
gpio_list = [17, 27, 22 , 5, 6, 13 , 26] 

bus = SMBus(1)

Ain0 = 0x00
Samples = 100
setup()
diff_max = 10
while 1:

    inputMax = 0
    inputMin = 255
    value = list()
    bus.write_byte(0x48,0x40|Ain0)
    bus.read_byte(0x48)
    bus.read_byte(0x48)
    for i in range(Samples):
	value.append(bus.read_byte(0x48))
	inputMin = min(inputMin, value[i])
    	inputMax = max(inputMax, value[i])

    #print value	
    diff = (inputMax - inputMin)
    #print diff	
    blink = diff/5
    diff_max = diff_max*0.9 + diff*0.1 + 2
    #print blink
    led_n(blink)

   # led_n(int(len(gpio_list)*(diff/diff_max)))






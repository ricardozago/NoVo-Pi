import wiringpi
from smbus import SMBus
from time import sleep


def mean(number_list):

    return float(sum(number_list)/len(number_list))
 




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
global_samples = 300
local_samples = 30
setup()
diff_max = 10
div = 5
blink = 0
norm = 1
while 1:

    inputMax = 0
    inputMin = 255
    value = list()
    bus.write_byte(0x48,0x40|Ain0)
    bus.read_byte(0x48)
    bus.read_byte(0x48)
    for i in range(global_samples):
	value.append(bus.read_byte(0x48))
#	inputMin = min(inputMin, value[i])
#    	inputMax = max(inputMax, value[i])
    global_mean = mean(value) #Global mean for compare 

    #print 'global_mean: {}'.format(global_mean)
    for j in range(global_samples):   
        
        value = list()
        bus.write_byte(0x48,0x40|Ain0)
        bus.read_byte(0x48)
        bus.read_byte(0x48)
        for i in range(local_samples):
	    value.append(bus.read_byte(0x48))
        
        local_mean = mean(value)
        diff = local_mean - global_mean  
        print diff

        diff_final = int(diff/norm)

        #if diff > 0:
         #   blink =  4 + int(diff)/norm
            
        #else:
         #   blink = 4 - int(diff)/norm
      
#       print blink
     #   print 'local_mean: {}'.format(local_mean)

        led_n((blink + diff_final)%7 + 1)
        blink = blink + diff_final

    

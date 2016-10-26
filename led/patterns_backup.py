import wiringpi
from time import sleep

#Need sudo permission for using wiringpi

def setup():

    wiringpi.wiringPiSetupGpio()	
    for gpio in gpio_list:	
        wiringpi.pinMode(gpio,1) #output pins
		
def led_pattern(gpio_list, delay = 0.5, led_value = True,
                fowarding = True):
	
    if fowarding:
        for gpio in gpio_list:
            wiringpi.digitalWrite(gpio, led_value)
	    sleep(delay)
    else:
        for gpio in reversed(gpio_list):
            wiringpi.digitalWrite(gpio, led_value)
	    sleep(delay)
			
def start():

    led_pattern(gpio_list)
    led_pattern(gpio_list, 0, False)	

def stop():
	
    led_pattern(gpio_list, 0)	
    sleep(0.5)
    led_pattern(gpio_list, led_value = False, fowarding = False)		

def restart():

    stop()
    start()

# Pins used to make the 'V' shaped LEDs blink
gpio_list = [17, 27, 22 , 5, 6, 13 , 26] 
setup()

if __name__ == '__main__':

    print 'Testing patterns'

    print 'Start'

    start()

    print 'Stop'

    stop()

    print 'Restart'
    
    restart()












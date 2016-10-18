import wiringpi
from time import sleep


gpio_list = [17, 27, 22 , 5, 6, 13 , 26] #pins used to make the 'V' shaped LEDs blink

def setup():

	wiringpi.wiringPiSetupGpio()	
	for gpio in gpio_list:	
		wiringpi.pinMode(gpio,1) #output pins
		
def led_pattern(list gpio_list, float delay = 0.5, bool led_value = True,bool fowarding = True):
	
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
	led_pattern(gpio_list, False, False)		

def restart():

	led_stop()
	led_start()
	
if __name__ == '__main__':

	setup()

	start()

	stop()

	restart()












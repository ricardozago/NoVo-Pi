import wiringpi
from time import sleep


#wiringpi.wiringPiSetup()

gpio_list = [17, 27, 22 , 5, 6, 13 , 26]


def setup():

	wiringpi.wiringPiSetupGpio()
	
	for gpio in gpio_list:
	
		wiringpi.pinMode(gpio,1) #output pins

def start():

	for gpio in gpio_list:
		
		wiringpi.digitalWrite(gpio,1)	
		
		sleep(0.5)

	for gpio in gpio_list:
		
		wiringpi.digitalWrite(gpio,0)	
		

def stop():

	for gpio in gpio_list:
		
		wiringpi.digitalWrite(gpio,1)	
		

	sleep(0.5)

	for gpio in reversed(gpio_list):
				
		wiringpi.digitalWrite(gpio,0)

		sleep(0.5)

def restart():

	led_stop()
	led_start()



if __name__ == '__main__':

	setup()

	start()

	stop()

	restart()












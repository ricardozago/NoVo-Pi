import wiringpi
from time import sleep
import argparse


#Need sudo permission for using wiringpi

def get_args():
        
    # Parse the command line into 'True/False' values.
    parser = argparse.ArgumentParser(description="Select led pattern")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-a', '--activate', action='store_true', help = 'Start pattern', required=False)
    group.add_argument('-s', '--stop', action='store_true', help = 'Stop pattern', required=False)
    group.add_argument('-r', '--restart', action='store_true', help = 'Restart pattern', required=False)
    group.add_argument('-b', '--boot', action='store_true', help = 'Start pattern', required=False)
    group.add_argument('-w', '--wlan0_ip_found', action='store_true', help = 'Start pattern', required=False)
    group.add_argument('--server', action='store_true', help = 'Start pattern', required=False)
    
    # args it is a namespace
    args = parser.parse_args()
    return args

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

def boot():

    led_pattern(gpio_list, delay = 1.0)
    led_pattern(gpio_list, delay = 0.0, led_value = False, fowarding=False)
    sleep(1)

def wlan0_ip_found():

    #Blink fast

    for i in range(5):

        led_pattern(gpio_list, delay = 0.1)
        led_pattern(gpio_list, delay = 0.1, led_value=False, fowarding=False)

    sleep(1)

def server():

    led_pattern(gpio_list, delay = 0.0)
    #led_pattern(gpio_list, delay = 0.0, led_value=False)	

# Pins used to make the 'V' shaped LEDs blink
gpio_list = [17, 27, 22 , 5, 6, 13 , 26] 
setup()

args = get_args()

if args.activate:
     start()        
elif args.stop:
    stop()                                                                            
elif args.restart:
    stop()
    start()
elif args.boot:
    boot()
elif args.wlan0_ip_found:
    wlan0_ip_found()
elif args.server:
    server()

#if __name__ == "__main__":

  #  start()
 #   stop()
    













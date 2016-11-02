import wiringpi
from smbus import SMBus
from time import sleep
import numpy as np
from random import randint, uniform
import os
import jsonrpclib

#Need sudo permission for using wiringpi

def setup():
    #setup LED pins 
    wiringpi.wiringPiSetupGpio()		
    for gpio in gpio_list:	
        wiringpi.pinMode(gpio,1) #output pins


def set_led(n = 0):

    if n < 0: n = 0
    if n > 7: n = 7
    #Erase all
    for gpio in gpio_list:	    	
        wiringpi.digitalWrite(gpio,0)
    #Set the offset
    for i in range(n):
        wiringpi.digitalWrite(gpio_list[i],1)


def jiggle(pace = 'small'):

    if pace == 'small':
        set_led(offset - 1)
        set_led(offset + 1)        
    elif pace == 'big':
        set_led(offset - 2)
        set_led(offset + 2)

# Pins used to make the 'V' shaped LEDs blink
gpio_list = [17, 27, 22 , 5, 6, 13 , 26]
ip = None
server = None
setup()
#setup localhost to get Mopidy status
ip = os.environ.get('MOPIDYSERVER', '127.0.0.1:6680')
server = jsonrpclib.Server('http://{}/mopidy/rpc'.format(ip))

bus = SMBus(1)
Ain0 = 0x00
local_samples = 100
global_samples = 300
list_global_samples = []
list_local_samples = []
mean_global = 255/2
std_global = 30
mean_local = mean_global
std_local = std_global

while 1:

    #global statistics
    
    if len(list_global_samples) == global_samples:
        sample_array = np.array(list_global_samples)
        mean_global = np.mean(sample_array)
        std_global = np.std(sample_array)
        list_global_samples = []
	
    #local statistics
    bus.write_byte(0x48,0x40|Ain0)
    bus.read_byte(0x48)
    bus.read_byte(0x48)
    
    for i in range(local_samples):
	list_local_samples.append(bus.read_byte(0x48))
	list_global_samples.append(list_local_samples[i])
    sample_array = np.array(list_local_samples)
    mean_local = np.mean(sample_array)
    std_local = np.std(sample_array)
    list_local_samples = []

    #Compare statistics
    
    if mean_local < mean_global - 2 * std_global: 
        offset = 2
    elif (mean_local >= mean_global - 2 * std_global) and (mean_local < mean_global - 1 * std_global):
        offset = 3
    elif (mean_local >= mean_global - 1 * std_global) and (mean_local < mean_global):
        offset = 4
    elif (mean_local >= mean_global ) and (mean_local < mean_global + 1 * std_global):
        offset = 5
    elif (mean_local >= mean_global + 1 * std_global) and (mean_local < mean_global + 1 * std_global):
        offset = 6
    elif (mean_local >= mean_global + 2 * std_global):
        offset = 7

    #Blink LEDs if music is playing
        
    if server.core.playback.get_state() == 'playing':

        #threshold for silence during music playing
        
        if mean_global > 0.05: 
            set_led(offset)
            if std_local < std_global:
                jiggle('small')
                offset = randint(0, 7)
                jiggle('small')
            else:
                jiggle('big')
                offset = randint(0, 7)
                jiggle('big')
            sleep(uniform(0, 0.2))
        else: set_led(0)
    else: set_led(0)
        
        






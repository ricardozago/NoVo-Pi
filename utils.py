import subprocess
import argparse
import threading
from time import sleep


def get_args():
        
    # Parse the command line into 'True/False' values.
    parser = argparse.ArgumentParser(description="Coordinate NoVo Pi")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-a', '--activate', action='store_true', help = 'Start NoVo Pi', required=False)
    group.add_argument('-s', '--stop', action='store_true', help = 'Stop NoVo Pi', required=False)
    group.add_argument('-r', '--restart', action='store_true', help = 'Restart NoVo Pi', required=False)
    
    # args it is a namespace
    args = parser.parse_args()
    return args


def start():

    active_flag = False
    #Check if module is already activated
    proc_1 = subprocess.Popen(['pgrep', '-f', 'mopidy'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc_1.communicate()
    proc_1.wait()
    
    if out != '':
        active_flag = True
    #Activate module
    if active_flag == False:
        proc_2 = subprocess.call(['sudo', 'python', '/home/pi/Documents/NoVo-Pi/led/patterns.py', '-a'])
        thread_1 = threading.Thread(target=start_mopidy, args=())        
        thread_2 = threading.Thread(target=start_led_mic, args=())
        thread_1.start()
        #Give some time to setup the Mopidy server, before starting the LEDs.
        sleep(10) 
        thread_2.start()
        
        
def stop():

    active_flag = False

    #Check if module is already activated
    proc_1 = subprocess.Popen(['pgrep', '-f', 'mopidy'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc_1.communicate()
    proc_1.wait()      

    if out != '':
        active_flag = True

    #Stop module
    if active_flag == True:

        proc_1 = subprocess.call('./stop_script.sh', shell=True)
        proc_2 = subprocess.call(['sudo', 'python', '/home/pi/Documents/NoVo-Pi/led/patterns.py', '-s'])

        
def start_mopidy():

    proc_1 = subprocess.call(['/usr/bin/mopidy'])


def start_led_mic():

    proc_1 = subprocess.call(['sudo', 'python', '/home/pi/Documents/NoVo-Pi/led/led_by_mic/led_by_mic.py'])

    
if __name__ == '__main__':

    print 'This module is used by novo_pi.py'    

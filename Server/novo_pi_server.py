import subprocess
import re
from time import sleep


#Get current wlan0 IP

wlan0_ip_re = r'192.168.[0-9]*.[0-9]*'
wlan0_ip = " "
while not bool(re.match(wlan0_ip_re, wlan0_ip)):
    proc_1 = subprocess.call(['sudo', 'python', '/home/pi/Documents/novo_pi/led/patterns.py', '--boot'])
    proc_2 = subprocess.Popen(['/home/pi/Documents/novo_pi/Server/host_ip.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    wlan0_ip, err = proc_2.communicate()
        
proc_3 = subprocess.call(['sudo', 'python', '/home/pi/Documents/novo_pi/led/patterns.py', '--wlan0_ip_found'])

#Start server

proc_4 = subprocess.call(['sudo', 'python', '/home/pi/Documents/novo_pi/led/patterns.py', '--server'])

proc_4 = subprocess.call(['sudo', 'python', '/home/pi/Documents/novo_pi/novo_pi.py', '--activate'])     


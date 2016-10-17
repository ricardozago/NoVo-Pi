import subprocess
import argparse


def get_args():

    #Parse the command line into 'True/False' values.
    parser = argparse.ArgumentParser(description="Coordinate NoVo Pi")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-a', '--activate', action='store_true', help = 'Start NoVo Pi', required=False)
    group.add_argument('-s', '--stop', action='store_true', help = 'Stop NoVo Pi', required=False)
    group.add_argument('-r', '--restart', action='store_true', help = 'Restart NoVo Pi', required=False)
    
    #args it is a namespace
    args = parser.parse_args()
    return args
    
def main():

    args = get_args()  
        if args.activate:
		
        active_flag = False

        #Check if module is already activated
        proc_1 = subprocess.Popen(['pgrep', '-f', 'mopidy'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = proc_1.communicate()
        proc_1.wait()
        
        if out != '':

            active_flag = True
	
        #Activate module
        if active_flag == False:
		
            proc_2 = subprocess.call(['lxterminal', '-e','mopidy'])
                                
    elif args.stop:

	active_flag = False

        #Check if module is already activated
        proc_1 = subprocess.Popen(['pgrep', '-f', 'mopidy'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = proc_1.communicate()
        proc_1.wait()      
        if out != '':

            active_flag = True
        
        #Stop module
        if active_flag == True:
		
            proc_2 = subprocess.call('./bash_script.sh', shell=True)
                                                                            
    elif args.restart:

        _ = 1
	
main()

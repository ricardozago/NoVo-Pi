import utils
from time import sleep


if __name__ == '__main__':

    args = utils.get_args()
    
    if args.activate:
        utils.start()        
    elif args.stop:
        utils.stop()                                                                            
    elif args.restart:
        utils.stop()
        sleep(4)
        utils.start()

import threading
import time


def main(ssid,pwd,number):

    print(ssid)



class ThreadingExample(object):

    def __init__(self,ssid,pwd,number):
        thread = threading.Thread(target=main, args=(ssid,pwd,number))
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution




example = ThreadingExample(4,5,6)
print('Checkpoint')
print('Bye')
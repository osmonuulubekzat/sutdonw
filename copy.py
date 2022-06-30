import os
import time

def ShutDown():
    return os.system("shutdown now")


counter = 5
is_active = True
while is_active:
    print(counter, end='\r')
    counter -= 1
    if counter < 0:
        is_active = False
        ShutDown()
    time.sleep(1)


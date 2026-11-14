import screen_brightness_control as sbc
import datetime
import time
import sys
a = str(datetime.datetime.now().time())
hour = (a[0]+a[1])
while(True):
        if (int(hour) >= 8 and int(hour) < 12):
                a = str(datetime.datetime.now().time())
                hour = int(a[0]+a[1])        
                sbc.set_brightness(int(hour)*4)
                print(hour)
                time.sleep(1)
        else:
                sbc.set_brightness(100)
                break
sys.exit

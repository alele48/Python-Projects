import os
import time
from plyer import notification
ipl=['1.8.1.1','8.8.8.8','6.6.6.6']

run = True

try:
    while run:
        for ip in ipl:
            
            # pings ip address in the ipl list using cmd
            response = os.popen('ping '+ip).read()
            # checks if the network is down
            if 'Received = 4' not in response:
                notification.notify(title = 'Network',message =' Network ' + ip + ' is down',
                                    app_icon = None,
                                    timeout = 10,)
            time.sleep(10)
            
        #run=False
except KeyboardInterrupt:
    notification.notify(title = 'Keyboard Interruption!',message = "Do not press Ctrl + c.",
                        app_icon = None,
                        timeout = 10,)
    
            

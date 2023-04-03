import os
import time
import datetime
from tkinter import messagebox
from plyer import notification

# gets the date in Y/M/D H/M/S
date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

run = True

# checks for keyboard interruptions ctrl + c
try:
    while run:
        # path to CMI network switches
        f = open("//192.168.50.202/IT Department/Network Tech/listCMI.txt","r")
        
        for ip in f:
            # pings the ip addresses in the file using cmd
            response = os.popen("ping "+ip).read()
            # checks if the network is down
            if "Received = 4" not in response:
                # returns notification message if a network is down
                notification.notify(title = "Network",message ="Network Device "
                                    + ip + "is down @ " + date,
                                    app_icon = None,
                                    timeout = 10,)
            #time.sleep(10)
            
        #run=False
except KeyboardInterrupt:
    messagebox.showinfo("Keyboard Interrupt", "Ctrl + c was pressed")
    
    
                

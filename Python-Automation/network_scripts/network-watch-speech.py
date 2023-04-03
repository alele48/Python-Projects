import os
import time
import pyttsx3
import datetime
from tkinter import messagebox
from plyer import notification

#date =  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
engine = pyttsx3.init()
t = time.ctime()
device_type = "Network Device "

run = True
#ip_list = ["4.12.3.4", "10.176.31.100"]
# checks for keyboard interruptions ctrl + c
try:
    while run:
        # path to CMI network switches
        ip_list = open('//192.168.50.202/IT Department/Network Tech/listCMI.txt',"r")
        
        for ip in ip_list:
            # pings the ip addresses in the file using cmd
            response = os.popen('ping '+ip).read()
            # checks if the network is down
            if 'Received = 4' not in response:
                # returns message if a network is down
                notification.notify(title = device_type,message ='Network Device '
                                    + ip + 'is down @ ' + t,
                                    app_icon = None,
                                    timeout = 2,)
                # sets speed of speech
                engine.setProperty("rate", 150)
                # converts texts into speech
                engine.say(device_type + ip + " is down @ " + t)
                engine.runAndWait()
                
            '''
                w = open('test.txt', 'w')
                w.write("Network Device " +ip +" is down\n")
                w.close()
            else:
                w = open('test.txt', 'a')
                w.write("Network Device " +ip +" is up\n")
                w.close()
            '''  
                
            #time.sleep(10)
            
        run=False
except KeyboardInterrupt:
    messagebox.showinfo("Keyboard Interrupt", "Ctrl + c was pressed")



from tkinter import messagebox
import paramiko
import os
import time
import datetime
import pyttsx3
from plyer import notification

date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
engine = pyttsx3.init()
run = True
minute = 60
hour = minute * 60 
# redhat credentials
device_type = input("Enter device type: ")
host = input("Enter host: ")
username = input("Enter username: ")
password = input("Enter Password: ")
port = int(input("Enter port: "))
file = input("Enter file location: ")
redhat = {
    'device_type':device_type,
    'host':host,
    'username':username,
    'password':password,
    'port':port
    }

# checks for keyboard interruptions, whether a user presses ctrl + c
try:
    while run:
        SESSION = paramiko.SSHClient()
        SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        SESSION.connect(host,port=port, username=username, password=password,
                        allow_agent=False, look_for_keys=False)
        # starts an interactive shell session on the SSH server
        SESSION.invoke_shell()
        f = open(file,"r")
        t = time.ctime()
        for ip in f:
            stdin, stdout, stderr = SESSION.exec_command("ping -c 8 "+ip)
            # checks if the network is down
            one_line = ''
            
            for lines in stdout:
                lines = lines.strip('\n')
                one_line = one_line + lines
            
            is_down = one_line.find('8 received')
            print(is_down)
            
            if is_down == -1:
                notification.notify(title = "Network",message ='Network Device '
                                    + ip + 'is down @ ' + t,
                                    app_icon = None,
                                    timeout = 2,)
            
            '''
            if '1 received' not in one_line:
                # returns message if a network is down
                notification.notify(title = "Network",message ='Network Device '
                                    + ip + 'is down @ ' + t,
                                    app_icon = None,
                                    timeout = 2,)
            
            '''
        time.sleep(minute * 30)    
except KeyboardInterrupt:
    messagebox.showinfo("Keyboard Interruption", "Ctrl + c was pressed")
    

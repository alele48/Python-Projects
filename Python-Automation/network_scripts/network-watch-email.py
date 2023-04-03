import os
import time
import smtplib
import ssl
from email.message import EmailMessage
ipl=['1.8.1.1','8.8.8.8','6.6.6.6']

sender = 'hideo.michael@vectrus.com'
password = input("Password:")
receiver =  'hideom1994@gmail.com'
subject = "Network Test"


em = EmailMessage()
em['From'] = sender
em['To'] = receiver
em['Subject'] = subject

run = True
try:
    while run:
        for ip in ipl:
            
            # pings ip address in the ipl list using cmd
            response = os.popen('ping '+ip).read()
            # checks if the network is down
            if 'Received = 4' not in response:
                em.set_content("Network " + ip + " is down")
                with smtplib.SMTP(host='smtp-mail.outlook.com', port=587) as smtp:
                    smtp.starttls()
                    smtp.login(sender, password)
                    smtp.sendmail(sender, receiver, em.as_string())
            time.sleep(10)
            
        run=False
except KeyboardInterrupt:
    notification.notify(title = 'Keyboard Interruption!',message = "Do not press Ctrl + c.",
                        app_icon = None,
                        timeout = 10,)
           

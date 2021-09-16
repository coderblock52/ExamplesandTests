import urllib.request #import for url interaction

import smtplib, ssl #imports for sending emails

import time #import for time delays

from datetime import datetime

from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart

 

port = 465 #for SSL assuming using gmail account for notifications

email = input("Type your gmail including @gmail.com: ")

password = input("Type your password and enter: ")

sender_email = email

receiver_email = input("Type the receiver password: ")

 

message = MIMEMultipart("alternative")

message["Subject"] = "Site Down"

message["From"] = sender_email

message["To"] = receiver_email

 

text = """\

-----Site is Down-----"""

html = """\

<html>

  <body>

    <p><b>-----Site is Down-----</b><br>

    </p>

  </body>

</html>

"""

 

part1 = MIMEText(text, "plain")

part2 = MIMEText(html, "html")

 

message.attach(part1)

message.attach(part2)

 

 

#Create secure SSL context

context = ssl.create_default_context()

 

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:

               server.login(email, password)

              

 

               i = 1

               while i:

                              response = urllib.request.urlopen(https://meters.pacificoffice.com/)

                              status_code = response.getcode()

                              dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

                              if status_code == 200:

                                             print("Site code: " + str(status_code) + " at " + dt_string)

                              else:

                                             print("SITE DOWN: " + str(status_code) + " at " + dt_string)

                                             server.sendmail(sender_email, receiver_email, message.as_string()) #send email to receiver email

                                             time.sleep(300)

                              time.sleep(30)
import smtplib #source:youtube
from email.mime.text import MIMEText #source:youtube
from email.mime.multipart import MIMEMultipart #source:youtube
import random
import string

b = "awqweqwdswegtr2372974358!@#!@$@#%#^&&*>?:LQWEERYOPKMNBVFCXXAZSSDFDGGGLM<BXVCBVCcnmcn,QWEWREWRTTYTRUTYIUYOPLIIKMYJHBGEDWCSQW&^*(()"
c= [1,2,3,4,5] #tried with strings but they are immutable so then a LIST
for x in range(0,5):
    c[x] = random.choice(b)
d="".join(c)
print(type(d))
print("ENTER YOUR EMAIL ADDRESS")

user_email=input()
email="whatever@whatever.com"
password="lol_whatever"
send_to= user_email + "@gmail.com"
mail_subject="YOUR ONE TIME PASSWORD"
mail_message= d

msg=MIMEMultipart()
msg['From']= email
msg['To']=send_to
msg['Subject']=mail_subject

msg.attach(MIMEText(mail_message,'plain'))

server=smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(email,password)
text=msg.as_string()
server.sendmail(email,send_to,text)
server.quit()
print("sucessfully sent")
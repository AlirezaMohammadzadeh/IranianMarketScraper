import smtplib
from .constants import *

class SendEmail:
    def __init__(self, sender, receivers):
        self.SmtpObj = smtplib.SMTP('Mail.eways.co')
        self.sender = sender
        self.receivers = receivers

    def send_email(self,message):
        try:
            msg = f"Subject: {SUBJECT}\r\n\r\n{message}"
            self.SmtpObj.sendmail(self.sender,self.receivers,msg)
        except Exception as e:
            print(str(e))



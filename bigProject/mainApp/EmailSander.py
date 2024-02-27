import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
class EmailSender():
    _sender = "createreport@mail.ru"
    _senderPassword = "kQb3DGd8bJEu6pmhcPdv"
    _targetEmail: str
    _smtp = "smtp.mail.ru"
    _smtpPort = 465

    def __init__(self, targetEmail):
        self._targetEmail = targetEmail
    def SendEmail(self, subjectText, bodyText):
        msg = MIMEMultipart()
        msg['From'] = self._sender
        msg['To'] = self._targetEmail
        msg['Subject'] = subjectText

        body = bodyText
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP_SSL(self._smtp, self._smtpPort)
        server.set_debuglevel(False)
        server.login(self._sender, self._senderPassword)
        server.send_message(msg)
        server.quit()

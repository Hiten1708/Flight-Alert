from twilio.rest import Client
import smtplib

# This class is responsible for sending notifications with the deal flight details.


class NotificationManager:
    def __init__(self):
        self.account_sid = 'ACc14b5045a0ebd599dc10b5b49651ee3d'
        self.auth_token = '6bba245fe9a40f3bb11dc2e1c6b0d0a4'
        self.client = Client(self.account_sid, self.auth_token)

    def send_msg(self, msg):
        message = self.client.messages \
            .create(
                body=msg,
                from_='+19096717302',
                to='+16472078688'
            )

    def send_email(self, msg, email):
        username = "ranarajput1409@gmail.com"
        password = "H1t3np@tel"
        try:
            with smtplib.SMTP("smtp.gmail.com") as server:
                server.starttls()
                server.login(
                    user=username,
                    password=password
                )
                server.sendmail(
                    from_addr=username,
                    to_addrs=email,
                    msg=msg
                )
        except Exception as e:
            print(e)

import smtplib
from email.message import EmailMessage

MY_EMAIL = "YOUR-EMAIL-ADDRESS"
PASSWORD = "YOUR-GOOGLE-APP-PASSWORD"


class EmailManager:
    def __init__(self, to_address, product_name, product_price):
        self.to_address = to_address
        self.product_name = product_name
        self.product_price = product_price

    def send_mail(self):
        subject = "Amazon price alert"
        body = f"{self.product_name}is now ${self.product_price}"
        message = EmailMessage()
        message.add_header("From", MY_EMAIL)
        message.add_header("To", self.to_address)
        message.add_header("Subject", subject)
        message.set_payload(body, "utf-8")
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.send_message(message, from_addr=MY_EMAIL, to_addrs=self.to_address)

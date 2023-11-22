from abc import ABC, abstractmethod
import smtplib
import ssl
import os
from dotenv import load_dotenv

load_dotenv("./app/stock_tracker")

class ICommunication(ABC):

    def send_email(self, content: str,subject:str, address:str):
        raise NotImplementedError()
    
    def send_sms(self, content: str,subject:str, phone: str):
        raise NotImplementedError()
    
class Communication(ICommunication):

    EMAIL_PORT = 465
    EMAIL_HOST = "smtp-mail.outlook.com"

    def __init__(self) -> None:
        
        self.__email_addr = os.getenv("SENDER_EMAIL")
        self.__email_pwd = os.getenv("PASSOWORD_EMAIL")

    def send_email(self, content: str,subject:str, address:str):

        email_message = f"""
            Subject: {subject}

            {content}
        """

        ssl_context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.EMAIL_HOST, self.EMAIL_PORT, context=ssl_context) as server:

            server.login(
                user=self.__email_addr,
                password=self.__email_pwd
            )

            server.sendmail(self.__email_addr, address, email_message)

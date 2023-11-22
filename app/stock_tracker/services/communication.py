from abc import ABC, abstractmethod
import smtplib
import ssl
import os
from dotenv import load_dotenv

load_dotenv("./app/stock_tracker")

class ICommunication(ABC):

    def send_email(self, content: str,subject:str, address:str):
        raise NotImplementedError()

    
class Communication(ICommunication):

    EMAIL_PORT = 587
    EMAIL_HOST = "smtp-mail.outlook.com"

    def __init__(self) -> None:
        
        self.__email_addr = os.getenv("SENDER_EMAIL")
        self.__email_pwd = os.getenv("PASSOWORD_EMAIL")

    def send_email(self, content: str,subject:str, address:str):

        email_message = f"""Subject: {subject}

            {content}
        """.encode("utf-8")

        with smtplib.SMTP(self.EMAIL_HOST, self.EMAIL_PORT) as server:
            server.ehlo()
            server.starttls()

            server.login(
                user=self.__email_addr,
                password=self.__email_pwd
            )

            server.sendmail(self.__email_addr, address, email_message)
            server.quit()

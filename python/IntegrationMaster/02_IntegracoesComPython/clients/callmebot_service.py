import requests
import os
from dotenv import load_dotenv

load_dotenv()


class CallmeBot:

    def __init__(self):
        self.__base_url = 'https://api.callmebot.com/whatsapp.php?'
        self.__api_key = os.getenv('API_KEY')
        self.__phone_number = os.getenv('PHONE')
        self.__message = os.getenv('MESSAGE')
    
    def send_message(self, message):
        response = requests.get(
            url=f'{self.__base_url}phone={self.__phone_number}&text={self.__message}&apikey={self.__api_key}'
                    
        )
        print(response.text)
        return response.text
    
    
        

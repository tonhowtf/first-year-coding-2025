import requests


class CoinConversorService:

    def __init__(self):
        self.__base_url = 'https://economia.awesomeapi.com.br/json/last/'


    def converter(self, coin_origin, coin_target):
        r = requests.get(
            url=f"{self.__base_url}{coin_origin}-{coin_target}"
        )
        if r.status_code == 404:
            return r.json().get('message')
        return r.json().get(f'{coin_origin}{coin_target}').get('bid')



        
        
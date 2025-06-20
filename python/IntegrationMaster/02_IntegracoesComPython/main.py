from clients.callmebot_service import CallmeBot
from clients.conversor_service import CoinConversorService


conversor_service = CoinConversorService()
conversion = conversor_service.converter('BTC', 'BRL')


wpp_service = CallmeBot()
wpp_service.send_message(
    message=f'Cotação do Bitcoin: {conversion}'
)
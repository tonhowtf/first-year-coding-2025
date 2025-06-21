import requests
import uuid

from decouple import config

ACESS_TOKEN = config('ACESS_TOKEN')

BASE_URL = 'https://api.mercadopago.com'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {ACESS_TOKEN}',
    'X-Idempotency-Key': str(uuid.uuid4()),

}

payload = {
    'transaction_amount': 25,
    'description': 'Vip',
    'payment_method_id': 'pix',
    'payer': {
        'email': 'test_user_123@testuser.com',
        'identification': {
            'type': 'CPF',
            'number': '95749019047',
        },
    },
}

response = requests.post(
    url=f'{BASE_URL}/v1/payments',
    json=payload,
    headers=headers,

)

print(response.json())
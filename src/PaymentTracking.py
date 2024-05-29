import requests

KAJABI_API_KEY = 'API key'
KAJABI_API_URL = 'API URL'

def fetch_kajabi_payments():
    headers = {'Authorization': f'Bearer {KAJABI_API_KEY}'}
    response = requests.get(f'{KAJABI_API_URL}/payements', headers=headers)
    payments = reponse.json()
    return payments

def track_kajabi_payments():
    payments = fetch_kajabi_payments()
    for payments in payments:
        coupon_code = payment.get('coupon_code')
        if coupon_code:
            track_signup_with_code(coupon_code)
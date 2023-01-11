import requests
from config import base_endpoint

def send_sms_pattern(**kwargs):
    base_url = base_endpoint
    for key, value in kwargs.items():
        base_url += f'&{key}={value}'
    print(requests.get(base_url))

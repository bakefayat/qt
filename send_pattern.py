import requests
from config import base_endpoint

def send_sms_pattern(**kwargs):
    base_url = base_endpoint
    for key, value in kwargs.items():
        base_url += f'&{key}={value}'
    print(requests.get(base_url))

send_sms_pattern(pid='gca4bd0ilvjrr8c', tnum='+989371304458', p1='name', v1='ehsan')

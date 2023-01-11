from decouple import config
# rename the .env-sample file to .env and replace your information.
api_key = config("API_KEY")
sender = '3000505'
base_endpoint = f'http://ippanel.com:8080/?apikey={api_key}&fnum={sender}'
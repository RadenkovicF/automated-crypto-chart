import requests
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

while True:
    print("Symbol eingeben:")
    input = input()
    break

coinmarketcapapi_key = ""


# coinmarketapi für bestimmte Preise
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

parameters = {
    'convert': 'EUR',
    "symbol": input,
}

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': coinmarketcapapi_key,
}

session = Session()
session.headers.update(headers)

try:
    gesamt = 0
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    if data["status"]["error_code"] == 0:
        print(data["data"])

except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

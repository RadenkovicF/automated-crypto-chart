# Script aktuell exklusiv für Time, kann erweitert werden oder auch autmatisiert aus einer Liste
import requests
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from web3 import Web3
from prowlpush import push_prowl

time_alarm = 2500
#TODO: apikey, walletaddress ausfüllen
coinmarketcapapi_key = ""
mm_address = "x"
ledger_address = "y"

# kostenlose APIs um Preise auf der jeweiligen Chain abzufragen
url_avax = "https://api.snowtrace.io/api"

# contract address, findet sich in jeder doch
stime_contract_address = "0x136acd46c134e8269052c62a67042d6bdedde3c9"  # Memo

# Hier die coinmarketcap id der Token eintragen. Mit skript "getIdFromSymbol.py"
my_assets = {
    "TIME": "11585",
}

# coinmarketapi für bestimmte Preise
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
# parameters für die Abfrage mit der conmarketcap API
# Preise deafult in USD. Wenn USD gewünscht, einfach EUR zu USD wechseln oder vielleicht einfach löschen
# zu testen
parameters = {
    'convert': 'EUR',
    "id": "11585"
}

# header für die Abfrage mit coinmarket api
# @API_KEY
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': coinmarketcapapi_key,
}

# session coinmarketcap api
session = Session()
session.headers.update(headers)


# TIME (Avax)
w3 = Web3(Web3.HTTPProvider("https://api.avax.network/ext/bc/C/rpc"))
API_ENDPOINT = url_avax + "?module=contract&action=getabi&address=" + str(stime_contract_address)
r = requests.get(url=API_ENDPOINT)
response = r.json()

instance = w3.eth.contract(
    address=Web3.toChecksumAddress(stime_contract_address),
    abi=response["result"]
)
# Holen der amount vom wallet
# @ADDRESSE AENDERN!
time_amount = instance.functions.balanceOf(ledger_address).call()
time_amount_dec = time_amount / 1000000000


try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)

    # TIME
    current_price = int(data["data"][my_assets["TIME"]]["quote"]["EUR"]["price"])
    time_val = current_price * time_amount_dec

    if time_val > time_alarm:
        push_prowl(event="Time: " + str("{:.2f}".format(time_val)) + "€", appName="Crypto Ticker", description="")

except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

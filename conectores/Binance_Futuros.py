import logging
import requests

logger = logging.getLogger()

def get_contracts():

    response_object = requests.get("https://fapi.binance.com//fapi/v1/exchangeInfo")

    contracts = []

    for contract in response_object.json()['symbols']:
        contracts.a ppend(contract['pair'])

    return contracts

print(get_contracts())
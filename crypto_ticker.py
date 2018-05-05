# -*- coding: utf-8 -*-
from decimal import Decimal

import rumps
import requests

#pulling coinbase data
API_URL = 'https://www.coinbase.com/api/v2/prices/{}/spot?'

#change values as needed
COIN = 'ETH'
CURRENCY = 'GBP'
HODL = Decimal(1.12880498) #stake

EXEC_TIMER = 60  # refresh every 60 seconds
ROUND_SCALE = 2

class CryptoTicker(rumps.App):

    @rumps.timer(EXEC_TIMER)
    def pull_data(self, _):
        response = requests.get(API_URL.format(CURRENCY))
        coin_data = response.json()['data']

        amount_str = ''

        for data in coin_data:
            base = data['base']
            currency = data['currency']

            if base == COIN and currency == CURRENCY:
                amount_str = data['amount']

        current_price = Decimal(amount_str)

        current_stake = current_price.__mul__(HODL) #calc total worth of hold
        fee = current_stake.__mul__(Decimal(0.003)) #calc coinbase fee

        profit = current_price - (current_stake - fee) #calc total profit

        self.title = str(round(current_price, ROUND_SCALE)) + ' | ' + \
                     str(round(current_stake, ROUND_SCALE)) + ' | ' + \
                     str(round(profit,        ROUND_SCALE))

if __name__ == "__main__":
    CryptoTicker("Loading...").run() #debug=True

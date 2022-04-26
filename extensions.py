import json
import requests
from data_file import *


class CurrencyException(Exception):
    pass


class ExchangeCurrency:
    @staticmethod
    def verification_method(currency_start: str, currency_convertible: str, amount: str):
        if currency_start == currency_convertible:
            raise CurrencyException(f'Невозможно перевести одинаковые валюты {currency_start}.')

        try:
            currency_start_code = currency_dict[currency_start.lower()]
        except KeyError:
            raise CurrencyException(f'Не смог обработать валюту {currency_start}')

        try:
            currency_convertible_code = currency_dict[currency_convertible.lower()]
        except KeyError:
            raise CurrencyException(f'Не смог обработать валюту {currency_convertible}')

        try:
            amount = int(amount)
        except KeyError:
            raise CurrencyException(f'Не смог обработать количество {amount}')

        result = requests.get(
            f'https://min-api.cryptocompare.com/data/price?fsym={currency_start_code}&tsyms={currency_convertible_code}')
        total_result = json.loads(result.content)[currency_convertible_code] * int(amount)
        return total_result






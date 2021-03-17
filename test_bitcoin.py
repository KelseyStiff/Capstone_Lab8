import unittest 
from unittest import TestCase
from unittest.mock import patch 

import bitcoin


class TestBitcoin(TestCase):
    @patch('bitcoin.get_exchange_rate')
    def test_(self, mock_rates):
        mock_rate = 123.4567
        example_api_response = {'time': {'updated': 'Mar 17, 2021 16:59:00 UTC', 'updatedISO': '2021-03-17T16:59:00+00:00', 'updateduk': 'Mar 17, 2021 at 16:59 GMT'}, 'disclaimer': 'This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org', 'chartName': 'Bitcoin', 'bpi': {'USD': {'code': 'USD', 'symbol': '&#36;', 'rate': '55,341.0833', 'description': 'United States Dollar', 'rate_float': mock_rate}, 'GBP': {'code': 'GBP', 'symbol': '&pound;', 'rate': '39,851.1694', 'description': 'British Pound Sterling', 'rate_float': 39851.1694}, 'EUR': {'code': 'EUR', 'symbol': '&euro;', 'rate': '46,489.2217', 'description': 'Euro', 'rate_float': 46489.2217}}}
        mock_rates.side_effect = [example_api_response]
        converted = bitcoin.convert(100, mock_rate)
        expected = 12345.67
        self.assertEqual(expected, converted)


if __name__ == '__main__':
    unittest.main()
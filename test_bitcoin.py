import unittest 
from unittest import TestCase
from unittest.mock import patch 

import bitcoin

class TestBitcoin(TestCase):
    @patch('bitcoin.retrieve_data')
    def test_(self, mock_rates):
        mock_rate = 10
        example_api_response = {
                                "time": {
                                "updated": "Mar 17, 2021 18:26:00 UTC",
                                "updatedISO": "2021-03-17T18:26:00+00:00",
                                "updateduk": "Mar 17, 2021 at 18:26 GMT"
                                },
                                "disclaimer": "This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
                                "chartName": "Bitcoin",
                                "bpi": {
                                "USD": {
                                "code": "USD",
                                "symbol": "&#36;",
                                "rate": "56,635.0074",
                                "description": "United States Dollar",
                                "rate_float": mock_rate
                                },
                                "GBP": {
                                "code": "GBP",
                                "symbol": "&pound;",
                                "rate": "40,868.1045",
                                "description": "British Pound Sterling",
                                "rate_float": 40868.1045
                                },
                                "EUR": {
                                "code": "EUR",
                                "symbol": "&euro;",
                                "rate": "47,557.1520",
                                "description": "Euro",
                                "rate_float": 47557.152
                                }
                                }
                                }        
        mock_rates.side_effect = [example_api_response]
        
        converted = bitcoin.get_exchange_rate(100)
        expected = 1000
        self.assertEqual(expected, converted)


if __name__ == '__main__':
    unittest.main()
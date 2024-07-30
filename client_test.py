import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'stock': 'ABC', 'top_bid': {'price': 121.2}, 'top_ask': {'price': 120.48}},
            {'stock': 'DEF', 'top_bid': {'price': 120.34}, 'top_ask': {'price': 119.2}}
        ]

        for quote in quotes:
            dataPoint = getDataPoint(quote)
            self.assertEqual(dataPoint, (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                                         (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    def test_getDataPoint_calculatePriceBidLessThanAsk(self):
        quotes = [
            {'stock': 'XYZ', 'top_bid': {'price': 119.2}, 'top_ask': {'price': 121.48}},
            {'stock': 'PQR', 'top_bid': {'price': 118.34}, 'top_ask': {'price': 119.2}}
        ]

        for quote in quotes:
            dataPoint = getDataPoint(quote)
            self.assertEqual(dataPoint, (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                                         (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    def test_getRatio(self):
        price_a = 119.2
        price_b = 121.48
        self.assertEqual(getRatio(price_a, price_b), price_a / price_b)

        price_a = 0
        self.assertEqual(getRatio(price_a, price_b), 0)

        price_b = 0
        self.assertEqual(getRatio(price_a, price_b), None)  # or handle division by zero as per your implementation


if __name__ == '__main__':
    unittest.main()

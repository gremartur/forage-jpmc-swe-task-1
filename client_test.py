import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    top_bid1 = quotes[0]['top_bid']['price']
    top_ask1 = quotes[0]['top_ask']['price']
    self.assertEqual(getDataPoint(quotes[0]), (quotes[0]['stock'], top_bid1, top_ask1, (top_bid1 + top_ask1) / 2))

    top_bid2 = quotes[1]['top_bid']['price']
    top_ask2 = quotes[1]['top_ask']['price']
    self.assertEqual(getDataPoint(quotes[1]), (quotes[1]['stock'], top_bid2, top_ask2, (top_bid2 + top_ask2) / 2))


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    top_bid1 = quotes[0]['top_bid']['price']
    top_ask1 = quotes[0]['top_ask']['price']
    self.assertEqual(getDataPoint(quotes[0]), (quotes[0]['stock'], top_bid1, top_ask1, (top_bid1 + top_ask1) / 2))

    top_bid2 = quotes[1]['top_bid']['price']
    top_ask2 = quotes[1]['top_ask']['price']
    self.assertEqual(getDataPoint(quotes[1]), (quotes[1]['stock'], top_bid2, top_ask2, (top_bid2 + top_ask2) / 2))



  """ ------------ Add more unit tests ------------ """
  def test_getRatio(self):
    self.assertIsNone(getRatio(1, 0))




if __name__ == '__main__':
    unittest.main()

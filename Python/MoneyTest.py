# Todo リスト
# □ $5 + 10CHF = $10(レートが2:1の場合)
# ■ $5 * 2 = $10
# □ amountをprivateにする
# ■ Dollarの副作用どうする？
# □ moneyの丸め処理どうする？

import unittest
from Dollar import Dollar

class MoneyTest(unittest.TestCase):
  
    def testMultiplication(self):
        five = Dollar(5)
        product = five.times(2)
        self.assertEqual(10, product.amount)
        product = five.times(3)
        self.assertEqual(15, product.amount)

if __name__ == '__main__':
    unittest.main()
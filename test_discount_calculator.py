#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#   file: test_discount_calculator
#   date: 2014-11-16
#   author: jdenisco
#   email: james.denisco@genesys.com
#
# Copyright © 2014 jdenisco <james.denisco@genesys.com>
#

"""
Description:
"""

import unittest

from discount_calculator import calculate_discount

class DiscountCalculaterTest(unittest.TestCase):
    def testGoodDiscount(self):
        cost = calculate_discount(200, 10, 30)

        self.assertEqual(cost, 150)


    def testlessthencost(self):
        cost = calculate_discount(200, 75, 60)

        self.assertEqual(cost, 20)


    def testrelitive_discountgt100(self):
        cost = calculate_discount(200, 110, 10)

        self.assertEqual(cost, 20)

if __name__ == '__main__':
    unittest.main()

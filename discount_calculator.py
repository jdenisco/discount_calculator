#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#   file: discount_calculator
#   date: 2014-11-16
#   author: jdenisco
#   email: james.denisco@genesys.com
#
# Copyright © 2014 jdenisco <james.denisco@genesys.com>
#

"""
Description:
"""

def calculate_discount(item_cost, relative_discount, absolute_discount):
    """ Calculate Discount """
    percent_in_decimal = (float(relative_discount) / 100)
    relative_cost = (item_cost - (item_cost * percent_in_decimal))
    cost = (relative_cost - absolute_discount)
    return cost



def main():
   print(calculate_discount(200, 10, 30))


if __name__ == '__main__':
    main()

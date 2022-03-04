#!/urs/bin/env python3
"""
stockwatcher_tests
copyright Ciaran Farley 2022

tests to verify stockwatcher is working as expected
"""

import stockwatcher

testurl = input()

print(stockwatcher.scraper(testurl))
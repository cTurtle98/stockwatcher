#!/usr/bin/env python3
"""
tests.py
copyright Ciaran Farley 2022

simple script for testing my package
"""

import stockwatcher

test_url_store_ui_com_in_stock = "https://store.ui.com/collections/unifi-protect/products/unifi-protect-g4-ptz"

print(stockwatcher.scraper.scrape(test_url_store_ui_com_in_stock))
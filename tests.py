#!/usr/bin/env python3
"""
tests.py
copyright Ciaran Farley 2022

simple script for testing my package
"""

import stockwatcher

test_url_store_ui_com_in_stock = "https://store.ui.com/collections/unifi-protect/products/unifi-protect-g4-ptz"

test_url_store_ui_com_out_of_stock = "https://store.ui.com/collections/unifi-protect/products/unifi-video-g3-flex-camera"

if stockwatcher.scraper.scrape(test_url_store_ui_com_in_stock) == 1:
    print("succes in stock")
else:
    print("error in stock")

if stockwatcher.scraper.scrape(test_url_store_ui_com_out_of_stock) == 0:
    print("succes out of stock")
else:
    print("error out of stock")


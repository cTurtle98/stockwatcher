#!/urs/bin/env python3
"""
tests_stockwatcher.py
copyright Ciaran Farley 2022

tests to verify stockwatcher is working as expected
"""

from ..stockwatcher import stockwatcher

test_url_store_ui_com_in_stock = "https://store.ui.com/collections/unifi-protect/products/unifi-protect-g4-ptz"

stockwatcher.scraper.scrape(test_url_store_ui_com_in_stock)
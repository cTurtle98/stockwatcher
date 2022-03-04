"""
scraper.py
copyright Ciaran Farley 2022

functions for scraping specific websites
"""

from selenium import webdriver

driver = webdriver.Firefox()

def scrape(url):
    """
    finds stock status for url
    return 1 = in stock
    return 0 = out of stock
    return -1 = store not supported or error
    """

    if "store.ui.com" in url:
        return store_ui_com(url)
    else:
        return("-1")

def store_ui_com(url):
    """
    scraper for ubiquiti store
    """

    # load the url
    driver.get(url)

    # find the add to cart button div
    product_button = driver.find_element_by_css_selector("#bundleApp > div.bundleLogic.add16bottom.add16top > div.one-whole.flex.flex-wrap > div > div.flex.flex-grow-1 > div.comProduct__button.flex-grow-1.add8left")
    if "Add to Cart" in product_button.text:
        return("1")
    if "Sold Out" in product_button.text:
        return("0")
    
    return("-1")
"""
scraper.py
copyright Ciaran Farley 2022

functions for scraping specific websites
"""

from selenium import webdriver
import atexit

driver = webdriver.Firefox()

def exit_handler():
    driver.close()
atexit.register(exit_handler)

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

    status = driver.find_element_by_xpath("//meta[@itemprop='availability']").get_attribute("content")

    if "InStock" in status:
        return(1)
    elif "OutOfStock"in status:
        return(0)
    else:
        return(-1)

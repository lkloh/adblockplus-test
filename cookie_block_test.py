import time, sys                                                        # some prints                    # to press keys on a webpage
import shutil, errno
import os, platform                         # for running  os, platform specific function calls
from selenium import webdriver              # for running the driver on websites
from datetime import datetime               # for tagging log with datetime             
from selenium.webdriver.common.proxy import *       # for proxy settings
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException





fp = webdriver.FirefoxProfile()

"""disable cookies"""
fp.set_preference("network.cookie.cookieBehavior", 2);
fp.update_preferences();


driver = webdriver.Firefox(firefox_profile=fp)
print 'driver started'

driver.get("http://www.bbc.com/news")
time.sleep(100)

driver.quit() 









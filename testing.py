import time, sys                                                        # some prints                    # to press keys on a webpage
import shutil, errno
import os, platform                         # for running  os, platform specific function calls
from selenium import webdriver              # for running the driver on websites
from datetime import datetime               # for tagging log with datetime             
from selenium.webdriver.common.proxy import *       # for proxy settings
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

proxy = 'proxy.pdl.cmu.edu:8080'
sproxy = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': proxy,
    'ftpProxy': proxy,
    'sslProxy': proxy,
    'noProxy': '' # set this value as desired
})

profile = ""
if (platform.system()=='Linux'):
    print 'Linux profile!'
    profile = 'extension/firefox_profiles/linux_profile.default'
elif (platform.system()=='Darwin'):
    profile = 'extension/firefox_profiles/macos_profile.default'
fp = webdriver.FirefoxProfile(profile)
fp.set_preference("signatures.required", False)
fp.set_preference('browser.helperApps.neverAsk.accept', True)
extension = 'extension/firefox/adblock_plus_easylist.xpi'
fp.add_extension(extension)

driver = webdriver.Firefox(proxy=sproxy, firefox_profile=fp)
print 'driver started'

driver.get('https://www.google.com/')
time.sleep(5)

driver.quit() 









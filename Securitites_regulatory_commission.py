import re
import urllib.request
import threading
from bs4 import BeautifulSoup

hosturl = 'http://disclosure.szse.cn/m/drgg.htm'

data = urllib.request.urlopen(hosturl).read().encode('utf-8')
print(data)

# search0425.js - suggest.js
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter the link- ')
position = int(input("Enter position:"))
repeat = int(input("How many times to repeat:"))


while repeat != 0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
    tags = soup('a')
    #downlow was an error, positioning in python starts from 0, while in excercise from 1
    url = tags[position-1].get('href',None)
    print(url)
    repeat = repeat-1

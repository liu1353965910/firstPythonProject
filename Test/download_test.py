# -*- coding: UTF-8 -*-
from urllib.error import HTTPError
from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

try:
    html = urlopen("http://www.pythonscraping.com")
except HTTPError as e:
    print(e)

bs_obj = BeautifulSoup(html, "html.parser")
image_location = bs_obj.find("div", {"class:", "field-item even"}).find("a").find("img")["src"]
urlretrieve(image_location, "logo.jpg")



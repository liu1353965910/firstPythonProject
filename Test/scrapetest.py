# -*- coding: UTF-8 -*-
import re
from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup

# try:
#     html = urlopen("http://www.pythonscraping.com/pages/page1.html")
#     if html is None:
#         print("URL is not found")
#     else:
#         bsObj = BeautifulSoup(html.read(), "html.parser")
#         print(bsObj.h1)
# except HTTPError as e:
#     print(e)
# else:
#     pass


# def getTitle(url):
#     """getTitle from url"""
#     try:
#         html = urlopen(url)
#     except HTTPError as e:
#         print(e)
#         return None
#     try:
#         bsObj = BeautifulSoup(html.read(), "html.parser")
#         title = bsObj.body.h1
#     except AttributeError as e:
#         print(e)
#         return None
#     return title
#
#
# title = getTitle("http://www.pythonscraping.com/pages/page1.html")
# if title == None:
#     print("Title is not found")
# else:
#     print(title)


# html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
# bsObj = BeautifulSoup(html, "html.parser")
# nameList = bsObj.findAll("span", {"class": "green"})
# for name in nameList:
#     print(name.get_text())


html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

# for child in bsObj.find("table", {"id": "giftList"}).children:
#     print(child)
#
# for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
#     print(sibling)

images = bsObj.findAll("img", {"src": re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for image in images:
    print(image.attrs["src"])



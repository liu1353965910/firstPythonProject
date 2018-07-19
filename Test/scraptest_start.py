# -*- coding: UTF-8 -*-
from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
import datetime

random.seed(datetime.datetime.now())

pages = set()


def get_links(article_url):
    try:
        html = urlopen("https://baike.baidu.com"+article_url)
    except HTTPError as e:
        print(e)
        return None

    try:
        bs_obj = BeautifulSoup(html, "html.parser")
        result = bs_obj.findAll("a", href=re.compile("^(/item/)"))
    except AttributeError as e:
        print(e)
        return None
    return result


links = get_links("/item/%E5%88%98%E5%BE%B7%E5%8D%8E/114923")

while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle)
else:
    print("found not")



# -*- coding: UTF-8 -*-
import re
from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup


pages = set()


def get_links(page_url):
    global pages
    try:
        html = urlopen("https://baike.baidu.com"+page_url)
    except HTTPError as e:
        print(e)
        return None

    try:
        bs_obj = BeautifulSoup(html, "html.parser")
        for link in bs_obj.findAll("a", href=re.compile("^(/item/)")):
            if "href" in link.attrs:
                if link.attrs["href"] not in pages:
                    new_page = link.attrs["href"]
                    print(new_page)
                    pages.add(new_page)
                    get_links(new_page)
    except AttributeError as e:
        print(e)
        return None


get_links("")

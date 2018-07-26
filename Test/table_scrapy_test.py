# -*- coding: UTF-8 -*-
from urllib.request import urlopen

from bs4 import BeautifulSoup
import csv

html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html, "html.parser")
table = bsObj.findAll("table", {"class", "wikitable"})[0]
rows = table.findAll("tr")
csvFile = open("editor.csv", "w+", newline="", encoding="utf-8")
writer = csv.writer(csvFile)
try:

    for row in rows:
        csvRow = []
        for col in row.findAll(["td", "th"]):
            csvRow.append(col.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()


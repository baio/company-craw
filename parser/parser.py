# -*- coding: utf-8 -*-

__author__ = 'baio'
from bs4 import BeautifulSoup
import re

def extract_text(str_fname_in, str_fname_out):

    with open(str_fname_in) as f:

        content = f.read()

    soup = BeautifulSoup(content)

    soup = BeautifulSoup(soup.prettify())

    txt = soup.get_text("\n", strip=True)
    txt = txt.encode("utf-8")

    txt = re.sub("\(", " ( ", txt)
    txt = re.sub("\)", " ) ", txt)
    txt = re.sub("\.", " . ", txt)
    txt = re.sub(",", " , ", txt)
    txt = re.sub(":", " : ", txt)
    txt = re.sub(";", " ; ", txt)
    txt = re.sub("«", " « ", txt)
    txt = re.sub("»", " »", txt)

    with open(str_fname_out, "w+") as f:

        f.write(txt)

extract_text("c:/dev/company-craw/store/raw/doc1.htm", "c:/dev/company-craw/store/parsed/doc1.txt")
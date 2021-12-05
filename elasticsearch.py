import re
import requests
import json
from elasticsearch import Elasticsearch
from bs4 import BeautifulSoup
es = Elasticsearch(['http://ilkom.unila.ac.id/'])

url = "http://ilkom.unila.ac.id/"
r = requests.get(url)
requests=r.content

soup=BeautifulSoup(requests,'html.parser')
title = soup.findAll('h2', attrs={'class':'post-box-title'})
isi = soup.findAll('div', attrs={'class':'tb-text-wrap'})
    
doc = {
    'title': title,
    'isi': isi
}

es.index(index="title", doc_type="isi", id=1, document=doc)
res = es.get(index="title", doc_type="isi", id=1)
res

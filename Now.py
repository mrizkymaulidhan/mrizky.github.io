import requests
import datetime
import time
import json
from bs4 import BeautifulSoup

Terkini={
    "time":"",
    "kategori":"",
    "judul":"",
    "waktu":""
}

data = []

page = requests.get("https://www.republika.co.id/")
obj = BeautifulSoup(page.text,'html.parser');

for headline in obj.find_all('div', class_='conten1'):
    Terkini["kategori"] = headline.find('h1').text
    Terkini["judul"] = headline.find('h2').text
    Terkini["waktu"] = headline.find('div', class_='date').text
    localtime = time.asctime(time.localtime(time.time()))
    Terkini["time"] = localtime

    data.append (dict(Terkini))
    print(Terkini)

with open ("Terkini.json", "w") as write_file:
    json.dump(data, write_file, indent=4)

import requests,re
import bs4 as bs
import json
#<h1>([^<]+)</h1>
#<span class="type-string">"202.136.89.146:8080"</span>
#<span class="type-string">([^<]+)</span>

reqhor = requests.get('http://www.equibase.com/static/entry//AQU112517USA3-EQB.html')
supa = bs.BeautifulSoup(reqhor.text, 'lxml')
for tr in supa.find_all('tr'):
    tds = tr.find_all('td')
    print(len(tds))


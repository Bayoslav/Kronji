import requests

import bs4 as bs


print("Australia")

r = requests.get('http://www.equibase.com/static/foreign/entry/index.html?SAP=TN#Australia')
soup = bs.BeautifulSoup(r.text,'lxml')

tables = soup.find_all('table')

table = tables[1] #australijskitejbl
tr = table.find_all('tr')
    #Featured Tracks	Today	Tomorrow	Future	Past
length = len(tr)
eventlist = []
for i in range(1,length,1):
    tds = tr[i].find_all('td')
    #print(tds[1])
    name = tds[0].text
    print(tds[1])
    url = 'http://www.equibase.com' + tds[1].find('a').get('href')
    date = tds[1].find('a').text
    if(date==''):
        print("No event today at " + name)
    else:
        print("No event today at " + name)
    

        print(url)
        #url = 'http://www.equibase.com' + tds[1].find('a').get('href')
        events = {
            'date' : date,
            'name' : name,
            'url' : url,
        }
        eventlist.append(events)
print(eventlist)
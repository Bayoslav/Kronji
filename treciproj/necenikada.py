import requests
import bs4 as bs


r = requests.get('http://210.145.16.108/jair/SelectRaceYear.do?command=GO')

soup = bs.BeautifulSoup(r.text,'lxml')
fontic = soup.find_all('font', attrs={'color' : '#0000ff', 'size' : 3 })
datic = (fontic[2].text).replace('/', '')
print(datic)
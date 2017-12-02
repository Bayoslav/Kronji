import requests 
import bs4 as bs

url = 'http://210.145.16.108/jair/SelectRaceYear.do?command=GO'
#<font color="#0000ff" size="3">2017/11/26</font>
r = requests.get(url)

soup = bs.BeautifulSoup(r.text,'lxml')

fontic = soup.find_all('font', attrs={'color' : '#0000ff', 'size' : 3 })
print(fontic[2])
#rint(fontic.text)

textic = '2017/11/26'

if(fontic[2].text==textic):
    print("Medals in derry")
else:
    print('no')


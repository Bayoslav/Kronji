import bs4 as bs
import requests

r = requests.get('http://www.equineline.com/Free5XPedigreeNickingDisplay.cfm?page_state=DISPLAY_REPORT&reference_number=9665908')

soup = bs.BeautifulSoup(r.text,'lxml')
try:
    a = soup.find('a').get('href')
except:
    a=''
if(a=='mailto:help@equineline.com'):
    print("NO horse")
else:
    print("stvorena")
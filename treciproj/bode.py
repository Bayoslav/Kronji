import requests
import bs4 as bs
headers = {'user-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)', 'origin': 'https://www.equibase.com',
                'x-requested-with': 'XMLHttpRequest'}
url = 'http://www.equineline.com/Free5XPedigreeSearchResults.cfm?horse_name=Tactical%20Manuevre'

#r = requests.get(url,headers=headers)
#text = r.text
#print(text)
#kk = r.text.find(text)
tiem = "  09:50 "

a = tiem.find(':')
dudu = "      "
dd = dudu.find(':')
print(a)

print(dd)
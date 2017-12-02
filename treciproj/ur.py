import requests
import bs4 as bs 

r = requests.get('http://www.equineline.com/Free5XPedigreeSearchResults.cfm?horse_name=Jack')

soup = bs.BeautifulSoup(r.text,'lxml')
h4 = soup.find('h4')
print(h4)
if(str(h4)=='<h4><strong>No Matches Found</strong></h4>'):
    print("No name for that hors")
else:
    print("Hors has anama")
#print(soup)
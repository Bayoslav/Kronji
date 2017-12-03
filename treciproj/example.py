import requests
global date
import bs4 as bs 
from datetime import datetime
import pytz
import uuid
import json,time,django
from treciproj import settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "treciproj.settings")
django.setup()
from RaceApp.models import Country
global headers
headers = {'user-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)', 'origin': 'https://www.equibase.com',
                'x-requested-with': 'XMLHttpRequest'}
def get_proxy():
    bumbum = 'http://api.proxyrotator.com/?apiKey=xPEjwuFkAhRrX2v43ZgVzcMWpQ9Gfs8H'

    r = requests.get(bumbum)

    jsonik = json.loads(r.text)
    proxies = {
        'http' : 'http://' + jsonik['proxy'],
    }
    print(jsonik['proxy'])
    return proxies
def get_table(table):
    #soup = bs.BeautifulSoup(table,'lxml')
    i=0
    print("Table TEST")
    dictlist = []
    for tr in table.find_all('tr'):
            
            i+=1
            tds = tr.find_all('td')
            if(i==1):
                sire = (tds[0].text)
            if(i==3):
                dict = {
            'sire' : sire,
            'name' : tds[0].text,
            'foals' : tds[2].text,
            'starters' : tds[3].text.replace(" ", "").replace("(", ",").replace(")",""),
            'winners' :  tds[4].text.replace(" ", "").replace("(", ",").replace(")",""),
            'BW (%)' : tds[5].text.replace(" ", "").replace("(", ",").replace(")",""),
            'earnings' : tds[6].text.replace("$", "").replace(",",""),
            'ael' : tds[7].text,
                }
            # print(dict)
                dictlist.append(dict)
            if(i==5):
                sire = (tds[0].text)
            if(i==7):
                dict = {
                'sire' : sire,
                'name' : tds[0].text,
                'mares' : tds[1].text,
                'foals' : tds[2].text,
                'starters' : tds[3].text.replace(" ", "").replace("(", ",").replace(")",""),
                'winners' :  tds[4].text.replace(" ", "").replace("(", ",").replace(")",""),
                'BW (%)' : tds[5].text.replace(" ", "").replace("(", ",").replace(")",""),
                'earnings' : tds[6].text.replace("$", "").replace(",",""),
                'ael' : tds[7].text,
                }   
                #print(dict)
                dictlist.append(dict)
            if(i==9):
                sire = (tds[0].text)
            if(i==11):
                dict = {
                'sire' : sire,
                'mares' : tds[1].text,
                'foals' : tds[2].text,
                'starters' : tds[3].text.replace(" ", "").replace("(", ",").replace(")",""),
                'winners' :  tds[4].text.replace(" ", "").replace("(", ",").replace(")",""),
                'BW (%)' : tds[5].text.replace(" ", "").replace("(", ",").replace(")",""),
                'earnings' : tds[6].text.replace("$", "").replace(",",""),
                'ael' : tds[7].text,
                }   
                #print(dict)
                dictlist.append(dict)
    return(dictlist)
def get_horses(racelist):
    for race in racelist:
        ##proxies = get_proxy()
        horselist = []
        #http://www.equibase.com/static/entry/
        url = race['URL']
        try:
            reqhor = requests.get(url)
        except:
            time.sleep(6)
            reqhor = requests.get(url)
        supa = bs.BeautifulSoup(reqhor.text, 'lxml')
        for tr in supa.find_all('tr'):
            tds = tr.find_all('td')
        #print(type(tds))
            if(len(tds)==12 or len(tds)==11):
                #print(tds)
                horsename = tds[2].text.strip(' \t\n\r').strip()[:-4].replace(" ", "%20")
                #print(horsename)
                print("itsthis")
                horseurl = 'http://www.equineline.com/Free5XPedigreeSearchResults.cfm?horse_name=' + horsename + '&page_state=LIST_HITS&foaling_year=&dam_name=&include_sire_line=Y'
                print(horseurl)
                print('kauboj')
                while(1):
                    try:
                        ###proxies = get_proxy()
                        horsereq = requests.get(horseurl,headers=headers,timeout=9)
                    except:
                        print('error')
                        time.sleep(12)
                        horsereq = requests.get(horseurl,headers=headers,timeout=9)
                        continue
                    else:
                        print("mek")
                        break              
                soup = bs.BeautifulSoup(horsereq.text, 'lxml')
                h4 = soup.find('h4')
                print(h4)
                if(str(h4)=='<h4><strong>No Matches Found</strong></h4>'):
                    print("Horse doesn't exist in DB")
                    inftab = 'n/a'
                else:
                #print(soup)
                    try:
                        horsrl = soup.find('a').get('href')
                    except:
                        print("Captcha error")
                        time.sleep(12)
                        ###proxies = get_proxy()
                        #time.sleep(6)
                        while(1):
                            try:
                                ##proxies = get_proxy()
                                horsereq = requests.get(horseurl,headers=headers,timeout=9)
                                soup = bs.BeautifulSoup(horsereq.text, 'lxml')
                                horsrl = soup.find('a').get('href')
                            except:
                                continue
                            else:
                                break
                        #soup = bs.BeautifulSoup(horsereq.text, 'lxml') 
                    #h#orsrl = soup.find('a').get('href')
                    url = 'http://www.equineline.com/' + horsrl
                    start = url.find('reference_number=')
                    end = url.find('&registry')
                    refnum = url[start+17:end]
                    print(refnum)
                    link = 'http://www.equineline.com/Free5XPedigreeNickingDisplay.cfm?page_state=DISPLAY_REPORT&reference_number=' + refnum
                    #print(url)
                    #print(link)
                    while(1):
                        try:
                            ##proxies = get_proxy()
                            maker = requests.get(link,headers=headers,timeout=9)
                            supica = bs.BeautifulSoup(maker.text,'lxml')
                            table = supica.find('table')
                            if(table is None):
                                ##proxies = get_proxy()
                                #soup = bs.BeautifulSoup(r.text,'lxml')
                                try:
                                    a = supica.find('a').get('href')
                                except:
                                    a=''
                                if(a=='mailto:help@equineline.com'):
                                    print("NO horse")
                                    table='Notable'
                                else:
                                    print("stvorena")
                                    maker = requests.get(link,headers=headers,timeout=9)
                                    supica = bs.BeautifulSoup(maker.text,'lxml')
                                    table = supica.find('table')
                        except:
                            continue
                        else:
                            break
                    #print(supica)
                   # table = supica.find('table')
                    #print(table)
                    #print(type(table))
                    while(1):
                        try:
                            if(table is None):
                                time.sleep(6)
                                ##proxies = get_proxy()
                                raise EnvironmentError
                            else:
                                break
                        except:
                            while(1):
                                try:
                                    maker = requests.get(link,headers=headers,timeout=9)
                                except:
                                    continue
                                else:
                                    break
                            break

                            supica = bs.BeautifulSoup(maker.text,'lxml')
                            table = supica.find('table')
                        
                    if(table=='Notable'):
                        inftab = 'n/a'
                    else:
                        inftab = get_table(table)
                ud = str(uuid.uuid4())
                if(len(tds)==12): 
                    horsedict = {
                        'P#' : tds[0].text.strip(' \t\n\r').replace(" ", ""),
                        'PP' : tds[1].text,
                        'Name' : tds[2].text.strip(' \t\n\r').strip()[:-5],
                        'Claim' : tds[6].text,
                        'Jockey': tds[7].text,
                        'Wgt' : tds[8].text,
                        'Trainer' : tds[9].text,
                        'M/L' : tds[10].text,
                        'Info' : inftab,
                        'uuid' : ud,
                    }
                else:
                    horsedict = {
                        'P#' : tds[0].text.strip(' \t\n\r').replace(" ", ""),
                        'PP' : tds[1].text,
                        'Name' : tds[2].text.strip(' \t\n\r').strip()[:-5],
                        'Claim' : 'No claim',
                        'Jockey': tds[6].text,
                        'Wgt' : tds[7].text,
                        'Trainer' : tds[8].text,
                        'M/L' : tds[9].text,
                        'Info' : inftab,
                        'uuid' : ud,
                    }
                horselist.append(horsedict)
        race['Horses'] = horselist
        print("list: ", horselist)
    return racelist


def get_events():
    global date
    try:
        r = requests.get('http://www.equibase.com/static/entry/index.html?SAP=TN')
    except:
        time.sleep(6)
        r = requests.get('http://www.equibase.com/static/entry/index.html?SAP=TN')
    soup = bs.BeautifulSoup(r.text,'lxml')
    #print(soup)
    table = soup.find('table')
    #print(table)
    tr = table.find_all('tr')
    #Featured Tracks	Today	Tomorrow	Future	Past
    length = len(tr)
    eventlist = []
    for i in range(1,length,1):
        tds = tr[i].find_all('td')
        #print(tds[1])
        name = tds[0].text
        try:
            url = 'http://www.equibase.com' + tds[1].find('a').get('href')
            date = tds[1].find('a').text
        except:
            print("No event today at " + name)
        else:
            print(url)
            #url = 'http://www.equibase.com' + tds[1].find('a').get('href')
            events = {
                'date' : date,
                'name' : name,
                'url' : url,
            }
            eventlist.append(events)
    print(eventlist)
    get_races(eventlist)

def get_races(eventlist):
    for race in eventlist:
        url = race['url']
        try:
            r = requests.get(url)
        except:
            time.sleep(6)
            r = requests.get(url)
        racelist = []
        soup = bs.BeautifulSoup(r.text,'lxml')
        for tr in soup.find_all('table'):
            tds = tr.find_all('td')
            length = len(tds)
            for i in range(0,length,8):
                #print(tds[i])
                #print(tds)
                x = tds[2+i].text.strip(' \t\n\r')
            # print("X = " + x)
                #print(dir(x))
            # x = str(x)
                #print(type(x))
                x = x.replace(" ", "")
                url = tds[0+i].find('a')
                #print(url)
                url = 'http://www.equibase.com' + url.get('href')
                tabledic = {
                    'Race: ' : tds[0+i].text,
                    'URL' : url,
                    'Purse' : tds[1+i].text,
                    'Race Type' : x,
                    'Distance' : tds[3+i].text,
                    'Surface' : tds[4+i].text,
                    'Starters' : tds[5+i].text,
                    'Est. Post' : tds[6+i].text,
                    'Horses' : [],
                }
                #print(type(tabledic))
                racelist.append(tabledic)
        race['races'] = get_horses(racelist)
    jsonero = json.dumps(eventlist)
    print("DATE:", date) #datum
    o = Country('1','America',jsonero,date) #datum
    o.save()
    f = open('americano.json','w')
    f.write(jsonero)
    f.close()
    #horsrl = soup.find('a').get('href')
    noder = requests.put('https://konji-187909.appspot.com/api/regions/america', json=jsonero)
    #jsonero = json.dumps(eventlist)
    #print(jsonero)
    #f = open('racehelpme.json', 'w')
    #f.write(jsonero)
    #f.close()
                #horses['Horses'] = get_horses(horses)

    
#get_events()

while(1):
    #r = requests.get('https://www.equibase.com/static/entry/index.html')
    #soup = bs.BeautifulSoup(r.text,'lxml')
    aa = Country.objects.get(id=1)
    dated = aa.date
    try:
        r = requests.get('http://www.equibase.com/static/entry/index.html?SAP=TN')
    except:
        time.sleep(6)
        r = requests.get('http://www.equibase.com/static/entry/index.html?SAP=TN')
    soup = bs.BeautifulSoup(r.text,'lxml')
    #print(soup)
    table = soup.find('table')
    #print(table)
    tr = table.find_all('tr')
    #Featured Tracks	Today	Tomorrow	Future	Past
    length = len(tr)
    eventlist = []
    for i in range(1,length,1):
        tds = tr[i].find_all('td')
        #print(tds[1])
        name = tds[0].text
        try:
            url = 'http://www.equibase.com' + tds[1].find('a').get('href')
            baba = tds[1].find('a').text
        except:
            print("No event today at ")
        else:
            break
    if(dated==baba): 
        print("No new races for date ", dated) #proverava ako je dd jednak dd u u bazi ako jeste spava, ako nije zove event
        print("\nSleeping for 20 minutes")
        time.sleep(1200)
        continue 
    else:
        print("New race! Scraping.")
        get_events()

    
#get_events()

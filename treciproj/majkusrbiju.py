import requests,uuid
import time as tim
import bs4 as bs
import django,os 
from treciproj import settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "treciproj.settings")
django.setup()
from RaceApp.models import Country
import json
global fontic
headers = {'user-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)', 'origin': 'https://www.equibase.com',
                'x-requested-with': 'XMLHttpRequest'}

def get_table(table):
    #soup = bs.BeautifulSoup(table,'lxml')
    i=0
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
            'starters' : tds[3].text,
            'winners' :  tds[4].text,
            'BW (%)' : tds[5].text,
            'earnings' : tds[6].text,
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
            'starters' : tds[3].text,
            'winners' :  tds[4].text,
            'BW (%)' : tds[5].text,
            'earnings' : tds[6].text,
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
                'starters' : tds[3].text,
                'winners' :  tds[4].text,
                'BW (%)' : tds[5].text,
                'earnings' : tds[6].text,
                'ael' : tds[7].text,
                }   
                #print(dict)
                dictlist.append(dict)
    return dictlist             
#r = requests.get('http://210.145.16.108/jair/SelectRaceYear.do?command=GO',headers=headers)
def get_events(datic):
    global fontic
    formData = {
        'raceYmd' : datic,
        'command' : 'displayRaceList'
    }
    kk = requests.post('http://210.145.16.108/jair/SelectRace.do',headers=headers,data=formData)
    soup = bs.BeautifulSoup(kk.text,'lxml')
    fontic = datic
    #print(fontic[2])
    #print(soup)
    #print(time.strftime("%Y/%m/%d"))
    soup = soup.find('table', attrs={'width': 584})
    tr = soup.find_all('tr')
    #print(tr[0].find('strong'))
    td = tr[0].find_all('td', attrs={'width' : '32%'})
    events = []
    print(len(td))
    for i in range(0,len(td)):
        txt = td[i].find('strong').text
        if(txt == ''):
            print("nothing")
        else:
            event = {
                'name' : txt,
                'races' : []
            }
        events.append(event)
    print(events)
    get_races(events)
    
def get_races(events):
    global fontic
    formData = {
        'raceYmd' : 20171209,
        'command' : 'displayRaceList'
    }
    kk = requests.post('http://210.145.16.108/jair/SelectRace.do',headers=headers,data=formData)
    soup = bs.BeautifulSoup(kk.text,'lxml')
    #print(soup)
    #print(time.strftime("%Y/%m/%d"))
    soup = soup.find('table', attrs={'width': 584})
    tr = soup.find_all('tr')
    lop=0
    ev=0
    for trs in tr[1:len(tr)]:
        tds = trs.find_all('td')
        for i in range(0,len(tds),3):
            
            #tds0 - vremeprva, #tds1  uputstva za slanje linka 
            #tds2 - vremedruga, #tds3 uputstva za slanje linka
            time = tds[0+i].text.replace(" ","")
            inform = tds[1+i]
            
            a = inform.find('a') #informator za post rikvest
        #print(inform)
            #print(a)
            kek = (a.get('href')[19:400].replace("(","").replace(")","").replace(" ", "")).strip(' \t\n\r') #isto kao dolje
            kek = kek.split(',')
            nl = []
            for word in kek: #uklanja /n i ostalo
                word = word.strip(" \t\n\r ' ")
                #print(word)
                nl.append(word)
            res = {
                'command':'dispRaceResult',
                'raceY':nl[0],
                'raceMd':nl[1],
                'raceJoCd':nl[2],
                'raceKai':nl[3],
                'raceHi':nl[4],
                'raceNo':nl[5],
                'dataKbn':nl[6],
            }
            race = { 
                    'time' : time,
                    'instr' : res,
                    }
            uuu = int(i/3)
            events[uuu]['races'].append(race)
        
       # W#event[lop]['races'] = 
        #p#rint(res)
    for me in events:
       for race in (me['races']):
            #horselist = []
            #print(race['time'])
            no = race['instr']['raceNo'].replace(" ", "")
            print(race['time'] + " - " +  race['instr']['raceNo'])
    #print(events)
            if(no == ''):
                print("no race")
            else:

                url = 'http://210.145.16.108/jair/SelectDenma.do'
                #formData = {'command': 'dispRaceResult', 'raceY': '2017', 'raceMd': '1126', 'raceJoCd': '05', 'raceKai': '05', 'raceHi': '08', 'raceNo': '01', 'dataKbn': '7'}
                formData = race['instr']
                req = requests.post(url,data=formData)
                soup = bs.BeautifulSoup(req.text,'lxml')
                tablic = soup.find_all('table',attrs={'cellspacing' : 0, 'cellpadding' : 1, 'width' : 720, 'bgcolor' : '#ffffff', 'border' : 1})
                print(tablic)
                table = soup.find('table',attrs={'cellspacing' : 0, 'cellpadding' : 0, 'width' : 720, 'bgcolor' : '#ffffff', 'border' : 0})
                tr = table.find_all('tr')
                newtr = tablic[1].find_all('tr')
                length = len(tr)
                eventlist = []
                #print("kek", length)
                horselist = []
                for i in range(5,length,1):
                    print(i)
                    tds = tr[i].find_all('td')
                    newtds = newtr[i-4].find_all('td')
                    #print(newtds)
                    hor = newtds[4].find_all('font')
                    siredam = newtds[2].find_all('font')
                    print(tds[2].text + " " + tds[3].text + " Jockey: " + hor[0].text + " Trainer: " + hor[1].text + "Sire" + siredam[0].text + "dam" + siredam[1].text)
                    print("itsthis")
                    horseurl = 'http://www.equineline.com/Free5XPedigreeSearchResults.cfm?horse_name=' + tds[3].text  + '&page_state=LIST_HITS&foaling_year=&dam_name=&include_sire_line=Y'
                    print(horseurl)
                    print("itsthis")
                    while(1):
                        try:
                            ###proxies = get_proxy()
                            horsereq = requests.get(horseurl,headers=headers,timeout=9)
                        except:
                            print('error')
                            tim.sleep(12)
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
                            tim.sleep(12)
                            ###proxies = get_proxy()
                            #tim.sleep(6)
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
                                    tim.sleep(6)
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
                    horsedic = {
                        'P#' : tds[2].text,
                        'Name' : tds[3].text,
                        'Claim' : 'No claim',
                        'Wgt' : tds[5].text,
                        'Jockey' : hor[0].text,
                        'Trainer' : hor[1].text,
                        'Sire' : siredam[0].text,
                        'Dam' : siredam[1].text,
                        'info' : inftab,
                        'uuid' : ud,
                    }
                    print(horsedic)
                    horselist.append(horsedic)
                race['horses'] = horselist
            #print(horselist)
    print(events)
    #print(formData)
    #print(formData.get('raceYmd'))
    date =  (formData.get('raceYmd'))
    o = Country('4','Japan',events,fontic)
    o.save()
    f=open('nippon2.json','w')
    jsonero = json.dumps(events)
    f.write(jsonero)
    f.close()

    #print(events)
        #print(events)
                #for ev in range(0,len(events),2):
                
    

html = '''<td align="left" nowrap="" width="32%">
<a class="uline" href="javascript:doSubmit('2017',
                      '1126',
                      '05',
                      '05',
                      '08',
                      '11',
                      '7')">
<font color="#0000ff">11R
                      OPN (G1)
                      T2400</font></a></td>'''


'''
 #command:dispRaceResult
            'raceY':2017
            'raceMd':1015
            'raceJoCd':05
            'raceKai':04
            'raceHi':05
            'raceNo':01
            'dataKbn':7       '''    
        
while(1):
    obj  = Country.objects.get(id=4)
    dat = obj.date
    r = requests.get('http://210.145.16.108/jair/SelectRaceYear.do?command=GO')
    soup = bs.BeautifulSoup(r.text,'lxml')
    fontic = soup.find_all('font', attrs={'color' : '#0000ff', 'size' : 3 })
    datic = (fontic[2].text).replace('/', '')
    print(datic)
    if(dat!=datic):
        print("New race! Scraping")
        get_events(datic)
    else:
        print("No new events found, sleeping for 20 minutes")
        tim.sleep(1200)
    #get_events(datic)   
#get_life()
#print(fontic)
#cities = td[0].find('strong').text + "  " + td[1].find('strong').text


#print(soup)'''
'''for trs in tbody[2:len(tbody)]:
    print
    trs = trs.find('font').text.replace(" ", "")
    print(trs)'''
#trs = tbody.find_all('font')
#print(trs)
    
    


#print(fonts)
import bs4 as bs
import requests
d = 0/2
print("COUNT", d)
textic  = '''
      <tr align="left">
      
        
        <td nowrap="" align="left">
          10:00
          
        </td>
        
        <td nowrap="" align="left" width="32%">
          <a class="uline" href="javascript:doSubmit('2017',
                      '1126',
                      '05',
                      '05',
                      '08',
                      '01',
                      '7')">
                      <font color="#0000ff">1R
                      MDN
                      T1400</font></a></td>
      
      
      <td></td>
      
        
        <td nowrap="" align="left">
          09:50
          
        </td>
        
        <td nowrap="" align="left" width="32%">
        <a class="uline" href="javascript:doSubmit('2017',
                  '1126',
                  '08',
                  '05',
                  '08',
                  '01',
                  '7')">
                  <font color="#0000ff">1R
                  MDN
                  D1200</font></a></td>
      
      
      <td></td>
      
        
        <td nowrap="" align="left">
          
          
        </td>
        
        <td nowrap="" align="left" width="32%">
        <a class="uline" href="javascript:doSubmit('',
                  '',
                  '',
                  '',
                  '',
                  '',
                  '')">
                  <font color="#0000ff">
                  
                  </font></a></td>
      
      
      
      <td></td>
    </tr>
'''

racelist = []

soup = bs.BeautifulSoup(textic,'lxml')
tag = '''<td align="left" nowrap="">
</td>'''
trs = soup.find_all('tr')
#timedic = {'time': '> </td>'}
for td in trs:
    tds = td.find_all('td')
    print(len(tds))
    for i in range(0,len(tds),3):
        #print("hmh", tds[0+i].text)
        #print('hm2' + str(tds[0+i]))
        #print('hmh3')
        txtic = tds[0+i].text.replace(" ", "").replace(" ", "")
        print(type(txtic))
        if(txtic.find(':') == -1):
            print('FOUND IT')
            print(tds[0+i])
        else:
            racedict = {
                'time' : tds[0+i],
                #'commands' : tds[1+i],
            }
            print("\ncount: " + str(i/3) + '\n')
            #print(racedict)
            #print(tag)
            racelist.append(racedict)
print(racedict)


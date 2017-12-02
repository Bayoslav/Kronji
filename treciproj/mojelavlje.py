import json
import ast
import uuid
f = open('C:/Users/Filip/inbreds.json' , 'r')
ovde = f.read()
f.close()
jsonero = ast.literal_eval(ovde)
#"starters": "210 ( 70)", 
for event in jsonero:
    races = event.get('races')
    for race in races:
        for horse in race['Horses']:
            info = horse['Info']
            for dic in info:
                if(info=='n/a'):
                    break
                s = dic['starters'] 
                s = s.replace(" ", "").replace("(", ",").replace(")","")
                dic['starters'] = s
                win = dic['winners']
                win = win.replace(" ", "").replace("(", ",").replace(")","")
                dic['winners'] = win
                bw = dic['BW (%)']
                bw = bw.replace(" ", "").replace("(", ",").replace(")","")
                dic['BW (%)'] = bw 
                earnings = dic['earnings']
                earnings = earnings.replace("$", "").replace(",","")
                dic['earnings'] = (earnings)

print(jsonero)

jsonic = json.dumps(jsonero)
f=open('inbreds2.json','w')
f.write(jsonic)
f.close()



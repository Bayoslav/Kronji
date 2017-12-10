import json,time,django
from treciproj import settings
import os
import ast
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "treciproj.settings")
django.setup()
from RaceApp.models import Country
import requests
o = Country.objects.get(id=1)
f = open('aussies2.json','w')
#jsonic = f.read()
#dicti = ast.literal_eval(jsonic)
#dictionary = ast.literal_eval(o.dicts)
jsonero = json.loads(o.dicts)
jsonic = json.dumps(jsonero)
f.write(jsonic)
f.close()
headers = {'Content-Type' : 'application/json', 'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
r = requests.put('https://konji-187909.appspot.com/api/regions/america',json=jsonic,timeout=1200)
print(r.text)

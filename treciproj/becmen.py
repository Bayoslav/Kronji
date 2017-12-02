import json,time,django
from treciproj import settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "treciproj.settings")
django.setup()
from RaceApp.models import Country
import requests
o = Country.objects.get(id=1)

f = open('noclaim.json','w')
f.write(o.dicts)
f.close()
#r = requests.post('metiovdeurl',json=jsonero)
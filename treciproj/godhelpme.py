import json


s= "210 ( 70)"
s = s.replace(" ", "").replace("(", ",").replace(")","")

s = s.replace("(", ",")
s = s.replace(")","")

print(s)
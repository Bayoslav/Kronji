from django.shortcuts import render
import json
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

class Jsin(APIView):
    def get(self,request):
        f = open('kek.json','r')
        kk = f.read()
        jsonero = json.dumps(kk)
        f.close()
        return Response(jsonero)    
    
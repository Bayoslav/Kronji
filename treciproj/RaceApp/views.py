from django.shortcuts import render,redirect
from django.views import View
from rest_framework import viewsets
from . import serializers
#from django.contrib.auth import login, authenticate
from django.http import HttpResponse, JsonResponse
#from .forms import LoginForm, UserForm
from .models import Country
import ast,json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

class Table(APIView):
    jobcont = []
    def get(self,request,offset):
       ## f = open('racehelpme.json', 'r')
        ##kk = f.read()

        o = Country.objects.get(name=offset)
        kk = o.dicts
        #kk.replace('\ ', '')
        kk = json.loads(kk)
        print(kk)
        return Response(kk)



# Create your views here.

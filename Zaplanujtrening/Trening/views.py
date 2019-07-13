from django.shortcuts import render
from Zaplanujtrening import urls
from django.http import request
from django.views import View

class MainSite(View):
    def get(self,request):
        return render(request,"index.html")
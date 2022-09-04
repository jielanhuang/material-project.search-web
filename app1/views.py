from django.shortcuts import render
from django.shortcuts import HttpResponse
from app1 import models
#页面查询用户信息
def index(request):
    search_info = request.GET.get('bandGapName')
    if search_info:
        search_result = models.Calculations.objects.raw("select * from calculations where band_gap = '{}' limit 10000".format(search_info))
    else:
        search_result=[]
    return render(request, 'main.html', {'data': search_result})
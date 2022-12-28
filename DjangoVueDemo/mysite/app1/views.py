from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def index(req):
    return render(req,'1/index.html')

def touch(req):
    return render(req,'1/index.html')

def regist(req):
    uname = req.POST.get("username","")
    json_dict={}
    json_dict["code"]=200
    json_dict["msg"]="success" + uname
    return JsonResponse(json_dict)
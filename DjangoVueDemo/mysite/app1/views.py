from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json

def index(req):
    return render(req,'1/index.html')

def touch(req):
    return render(req,'1/index.html')

def regist(req):
    uname = req.POST.get("username","")
    print(req.body)
    print(uname)
    json_dict={}
    json_dict["code"]=200
    json_dict["msg"]="success " + json.loads(req.body)['username']
    return JsonResponse(json_dict)
from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import *
from .sqlparams import *
from .sqlcommands import *

# Create your views here.
def ludipDash(request):
    return render(request, 'themes/dashboard-ludip.html')

def ludipView(request):
    form = ludipForm()
    ludipList = ludip.objects.raw(fetchLudip())
    return render(request, 'themes/ludip.html',{'lform':form, 'ludipList':ludipList} )

def ludipJsonList(request):
    with connection.cursor() as cursor:
            cursor.execute(fetchLudip())
            rows = cursor.fetchall()
            
    tempRes = None
    jsonResultData = []

    for row in rows:
        tempRes = {
            'ludipId': row[0],
            'campus': row[1],
            'totalLandArea':row[2],
            'landUsed': row[3],
            'remainLand': row[4],
            'landUsedMap':row[5],
            'siteDevPlan': row[6],
            'remarks': row[7],
            'isActive': row[8]
        }
        jsonResultData.append(tempRes)
    return JsonResponse({"data":list(jsonResultData)}, safe=False)

def ludipSaveParams(request):
    cursor = connection.cursor()
    if(request.POST):
        form = ludipForm(request.POST)
        try:
            if form.is_valid():
                ludipParams["campus"] = form['campus'].value()
                ludipParams["totalLandArea"] = form['totalLandArea'].value()
                ludipParams["landUsed"] = form['landUsed'].value()
                ludipParams["remainLand"] = form['remainLand'].value()
                ludipParams["landUsedMap"] = form['landUsedMap'].value()
                ludipParams["siteDevPlan"]= form['siteDevPlan'].value()
                ludipParams["remarks"] = form['remarks'].value()
                ludipParams["isActive"] = 'Y'
                print("Debug: " + insertNewLudip(**ludipParams))
                form = ludipForm()
                cursor.execute(insertNewLudip(**ludipParams))
                return (JsonResponse({"Status": "Saved"}))
            else:
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

def lupidUpdateParams(request, id):
    cursor = connection.cursor()
    form = ludipForm(request.POST) 
    if(request.POST):
        try:
            if form.is_valid():
                ludipParams["ludipId"] = id
                ludipParams["campus"] = form['campus'].value()
                ludipParams["totalLandArea"] = form['totalLandArea'].value()
                ludipParams["landUsed"] = form['landUsed'].value()
                ludipParams["remainLand"] = form['remainLand'].value()
                ludipParams["landUsedMap"] = form['landUsedMap'].value()
                ludipParams["siteDevPlan"]= form['siteDevPlan'].value()
                ludipParams["remarks"] = form['remarks'].value()
                ludipParams["isActive"] = 'Y'
                print("Debug: " + updateLudip(**ludipParams))
                form = ludipForm()
                cursor.execute(updateLudip(**ludipParams))
                return (JsonResponse({"Status": "Updated"}))
            else:
                return JsonResponse({"Status":"Error"})
        except Exception as err:
                print(f"{type(err).__name__} was raised: {err}")
                return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

@csrf_exempt        
def lupidDeleteParams(request,id):
    cursor = connection.cursor()
    try:
        ludipParams["ludipId"] = id
        ludipParams["isActive"] = 'N'
        print("Debug: " + deleteLudip(**ludipParams))
        cursor.execute(deleteLudip(**ludipParams))
        return JsonResponse({"Status":"Deleted"})
    except Exception as err:
        print(f"{type(err).__name__} was raised: {err}")
        return JsonResponse ({"Error":err}) 


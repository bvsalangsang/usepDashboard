from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import *
from .sqlparams import *
from .sqlcommands import *

# Create your views here.

#campus
def campusView(request):
    form = campusForm()
    return render(request, 'themes/campus.html',{'form':form})

def campusJsonList(request):
    with connection.cursor() as cursor:
            cursor.execute(fetchCampus())
            rows = cursor.fetchall()
            
    tempRes = None
    jsonResultData = []

    for row in rows:
        tempRes = {
            'campId': row[0],
            'name': row[1],
            'isActive': row[2]
        }
        jsonResultData.append(tempRes)
    return JsonResponse({"data":list(jsonResultData)}, safe=False)

def saveUpdateCampusParams(request):
    cursor = connection.cursor()
    if(request.POST):
        form = campusForm(request.POST)
        try:
            if form.is_valid():
                gadCampusParams['campId'] = request.POST['campId']
                print(request.POST['campId'])
                gadCampusParams['name'] = form['name'].value()
                gadCampusParams['isActive'] = 'Y'
                print("Debug: " + insertUpdateCampus(**gadCampusParams))
                cursor.execute(insertUpdateCampus(**gadCampusParams))
                return (JsonResponse({"Status":"Saved"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})                 
    else:
        return JsonResponse({"Status":"Wrong Request"})

@csrf_exempt    
def deleteCampusParams(request,id):
    cursor = connection.cursor()
    try:
        gadCampusParams["campId"] = id
        gadCampusParams["isActive"] = 'N'
        print("Debug: " + deleteCampus(**gadCampusParams))
        cursor.execute(deleteCampus(**gadCampusParams))
        return JsonResponse({"Status":"Deleted"})
    except Exception as err:
        print(f"{type(err).__name__} was raised: {err}")
        return JsonResponse ({"Error":err})
    
#division
def divisionView(request):
    form = divisionForm()
    campusList = gadCampus.objects.raw(fetchCampus())
    return render(request, 'themes/division.html',{'form':form, 'campusList':campusList})

def divisionJsonList(request):
    with connection.cursor() as cursor:
            cursor.execute(fetchDivision())
            rows = cursor.fetchall()
            
    tempRes = None
    jsonResultData = []

    for row in rows:
        tempRes = {
            'divId': row[0],
            'campus':row[1],
            'name': row[2],
            'isActive': row[3]
        }
        jsonResultData.append(tempRes)
    return JsonResponse({"data":list(jsonResultData)}, safe=False)

def saveUpdateDivParams(request):
    cursor = connection.cursor()
    if(request.POST):
        form = divisionForm(request.POST)
        try:
            if form.is_valid():
                gadDivisionParams['divId'] = request.POST['divId']
                gadDivisionParams['campId'] = request.POST['campId']
                gadDivisionParams['name'] = form['name'].value()
                gadDivisionParams['isActive'] = 'Y'
                print("Debug: " + insertUpdateDivision(**gadDivisionParams))
                cursor.execute(insertUpdateDivision(**gadDivisionParams))
                return (JsonResponse({"Status":"Saved"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})                 
    else:
        return JsonResponse({"Status":"Wrong Request"})

@csrf_exempt    
def deleteDivParams(request,id):
    cursor = connection.cursor()
    try:
        gadDivisionParams["divId"] = id
        gadDivisionParams["isActive"] = 'N'
        print("Debug: " + deleteDivision(**gadDivisionParams))
        cursor.execute(deleteDivision(**gadDivisionParams))
        return JsonResponse({"Status":"Deleted"})
    except Exception as err:
        print(f"{type(err).__name__} was raised: {err}")
        return JsonResponse ({"Error":err})
    
#component
def componentView(request):
    form = componentForm()
    divList = gadDivision.objects.raw(fetchDivision())
    return render(request, 'themes/component.html',{'form':form, 'divList':divList})
    
def componentJsonList(request):
    with connection.cursor() as cursor:
        cursor.execute(fetchComponent())
        rows = cursor.fetchall()

    tempRes = None
    jsonResultdata = []

    for row in rows:
        tempRes = {
            'compId': row[0],
            'division': row[1],
            'desc':row[2],
            'isActive':row[3]
        }
        jsonResultdata.append(tempRes)
    return JsonResponse({"data":list(jsonResultdata)}, safe=False)

def getCompJsonList(request):
    gadDivisionParams['divId'] = request.GET.get('divId')
    with connection.cursor() as cursor:
        cursor.execute(getComponent(**gadDivisionParams))
        rows = cursor.fetchall()
    
    tempRes = None
    jsonResultdata = []

    for row in rows:
        tempRes = {
            'compId': row[0],
            'division': row[1],
            'desc':row[2],
            'isActive':row[3]
        }
        jsonResultdata.append(tempRes)

    return JsonResponse({"data":list(jsonResultdata)}, safe=False)

def saveUpdateCompParams(request):
    cursor = connection.cursor()
    if(request.POST):
        form = componentForm(request.POST)
        try:
            if form.is_valid():
                gadComponentParams['compId'] = request.POST['compId']
                gadComponentParams['divId'] = request.POST['divId']
                gadComponentParams['description'] = form['description'].value()
                gadComponentParams['isActive'] = 'Y'
                print("Debug: " + insertUpdateComponent(**gadComponentParams))
                cursor.execute(insertUpdateComponent(**gadComponentParams))
                return (JsonResponse({"Status":"Saved"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})                 
    else:
        return JsonResponse({"Status":"Wrong Request"})

@csrf_exempt    
def deleteCompParams(request,id):
    cursor = connection.cursor()
    try:
        gadComponentParams["compId"] = id
        gadComponentParams["isActive"] = 'N'
        print("Debug: " + deleteComponent(**gadComponentParams))
        cursor.execute(deleteComponent(**gadComponentParams))
        return JsonResponse({"Status":"Deleted"})
    except Exception as err:
        print(f"{type(err).__name__} was raised: {err}")
        return JsonResponse ({"Error":err})
    

#gad Details
def gadView(request):
    form = gadForm()
    campusList = gadCampus.objects.raw(fetchCampus())
    divList = gadDivision.objects.raw(fetchDivision())
    compList = gadComponent.objects.raw(fetchComponent())
    return render(request,'themes/gad.html',{'form':form,'campusList':campusList,'divList':divList,'compList':compList})

def gadJsonList(request):
    with connection.cursor() as cursor:
        cursor.execute(fetchGad())
        rows = cursor.fetchall()

    tempRes = None
    jsonResultdata = []

    for row in rows:
        tempRes = {
            'gadId': row[0],
            'campus': row[1],
            'division':row[2],
            'component':row[3],
            'series':row[4],
            'program':row[5],
            'female': row[6],
            'male':row[7],
            'total':row[8]
        }
        jsonResultdata.append(tempRes)
    return JsonResponse({"data":list(jsonResultdata)}, safe=False)

def saveUpdateGadDetails(request):
    cursor = connection.cursor()
    if (request.POST): 
        form = gadForm(request.POST)
        try:
            if form.is_valid():
                gadDetParams['gadId'] = request.POST['gadId']
                gadDetParams['campId'] = request.POST['campId']
                gadDetParams['compId'] = request.POST['compId']
                gadDetParams['series'] = form['series'].value()
                gadDetParams['program'] =form['program'].value()
                gadDetParams['female'] = form['female'].value()
                gadDetParams['male'] = form['male'].value()
                gadDetParams['total'] = request.POST['total']
                gadDetParams['isActive'] = 'Y'

                print("Debug: " + insertUpdateGadDetails(**gadDetParams))
                cursor.execute(insertUpdateGadDetails(**gadDetParams))
                return (JsonResponse({"Status":"Saved"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})

@csrf_exempt 
def deleteGadParams(request,id):
    cursor = connection.cursor()
    try:
        gadDetParams["gadId"] = id
        gadDetParams["isActive"] = 'N'
        print("Debug: " + deleteGad(**gadDetParams))
        cursor.execute(deleteGad(**gadDetParams))
        return JsonResponse({"Status":"Deleted"})
    except Exception as err:
        print(f"{type(err).__name__} was raised: {err}")
        return JsonResponse ({"Error":err})
    
def gadDashView(request):
    campusList = gadCampus.objects.raw(fetchCampus())
    divList = gadDivision.objects.raw(fetchDivision())
    return render(request,'themes/dashboard-gad.html',{'campusList':campusList,'divList':divList})

def gadDashAllView(request):
    return render(request,'themes/dashboard-gad-all.html')

def gadDashNewView(request):
    return render(request, 'themes/dashboard-gad-new.html')
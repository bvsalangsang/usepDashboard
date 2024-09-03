from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


from .forms import *
from .sqlparams import *
from .sqlcommands import *

from dashAnalyticApp.sqlcommands import fetchType
from dashAnalyticApp.models import refType

import json
# Create your views here.

# def index(request):  
#     return render(request, 'themes/dashboard.html')

#default dashboard
def dashboard(request):
    return render(request, 'themes/dashboard.html')


#strategic Dashboard
def stratDash(request):
    return render(request, 'themes/dashboard-strategic.html')

def demoDash(request):
    return render(request, 'themes/demo-dashstrat.html')

def dashAnnTargetJsonList(request):
    with connection.cursor() as cursor:
        cursor.execute(stratAnnualTargets())
        rows = cursor.fetchall()

    areas = {}
    objects_map = {}
    indicators_map = {}

    for row in rows:
        area_id = row[0]
        if area_id not in areas:
            areas[area_id] = {
                "areaId": row[0],
                "code": row[1],
                "area": row[2],
                "isActive": row[3],
                "objects": []
            }

        obj_id = row[4]
        if obj_id:
            if obj_id not in objects_map:
                obj = {
                    "sAreaId": row[0],
                    "objId": row[4],
                    "objCode": row[5],
                    "ObjName": row[6],
                    "isActive": row[7],
                    "indicator": []
                }
                areas[area_id]["objects"].append(obj)
                objects_map[obj_id] = obj
            else:
                obj = objects_map[obj_id]

            ind_id = row[8]
            if ind_id and ind_id not in indicators_map:
                ind = {
                    "objId": row[4],
                    "indId": row[8],
                    "refType": row[9],
                    "indCode": row[10],
                    "indDesc": row[11],
                    "isActive": row[12],
                    "sRef": row[13],
                    "blineData": row[14],
                    "targetPlan": row[15],
                    "yr2022": row[16],
                    "yr2023": row[17],
                    "yr2024": row[18],
                    "yr2025": row[19],
                    "yr2026": row[20],
                    "yr2027": row[21],
                    "ctrlNo": row[23]
                }
                obj["indicator"].append(ind)
                indicators_map[ind_id] = ind

    data = list(areas.values())
    return JsonResponse({"data": data}, json_dumps_params={'indent': 2})

def saveDashRecord(request):
    try:
        matricesParams['indId'] = request.POST['indId']
        matricesParams['reference'] = request.POST['reference']
        matricesParams['blineData'] = request.POST['baseline']
        matricesParams['targetPlan'] = request.POST['targetplan']
        matricesParams['yr2022'] = request.POST['yr2022']
        matricesParams['yr2023'] = request.POST['yr2023']
        matricesParams['yr2024'] = request.POST['yr2024']
        matricesParams['yr2025'] = request.POST['yr2025']
        matricesParams['yr2026'] = request.POST['yr2026']
        matricesParams['yr2027'] = request.POST['yr2027']
        matricesParams['isActive'] = 'Y'
        matricesParams['ctrlNo'] = request.POST['ctrlNo']
        print(insertMartrices(**matricesParams))
        cursor = connection.cursor()
        cursor.execute(insertMartrices(**matricesParams))
        return (JsonResponse({"Status": "Saved"}))
    except Exception as err:
        print(str(err))
        return JsonResponse({"Status": "Error", "Error": str(err)})

#yearly scorecard 
def scoreDash(request):
    return render(request,'themes/dashboard-scorecard.html')

def dashScorecardJsonList(request, year):
    with connection.cursor() as cursor:
        scorecardParams['targetyear'] = year
        cursor.execute(stratScorecards(**scorecardParams))
        rows = cursor.fetchall()

    areas = {}
    objects_map = {}
    indicators_map = {}

    for row in rows:
        area_id = row[0]
        if area_id not in areas:
            areas[area_id] = {
                "areaId": row[0],
                "code": row[1],
                "area": row[2],
                "isActive": row[3],
                "objects": []
            }

        obj_id = row[4]
        if obj_id:
            if obj_id not in objects_map:
                obj = {
                    "sAreaId": row[0],
                    "objId": row[4],
                    "objCode": row[5],
                    "ObjName": row[6],
                    "isActive": row[7],
                    "indicator": []
                }
                areas[area_id]["objects"].append(obj)
                objects_map[obj_id] = obj
            else:
                obj = objects_map[obj_id]

            ind_id = row[8]
            if ind_id and ind_id not in indicators_map:
                ind = {
                    "objId": row[4],
                    "indId": row[8],
                    "refType": row[9],
                    "indCode": row[10],
                    "indDesc": row[11],
                    "isActive": row[12],
                    "sRef": row[13],
                    "year": row[14],
                    "target": row[15],
                    "actual": row[16],
                    "variance": row[17],
                    "percentage": row[18],
                    "ctrlNo": row[20]
                }
                obj["indicator"].append(ind)
                indicators_map[ind_id] = ind

    data = list(areas.values())
    return JsonResponse({"data": data}, json_dumps_params={'indent': 2})

def saveScorecardParams(request):
    try:
        print(request.POST)
        scorecardParams['indId'] = request.POST['indId']
        scorecardParams['reference'] = request.POST['reference']
        scorecardParams['targetyear'] = request.POST['targetyear']
        scorecardParams['target'] = request.POST['target']
        scorecardParams['actual'] = request.POST['actual']
        scorecardParams['variance'] = request.POST['variance']
        scorecardParams['percentage'] = request.POST['percentage']
        scorecardParams['isActive'] = 'Y'
        scorecardParams['ctrlNo']  = request.POST['ctrlNo']
        print(insertNewScorecards(**scorecardParams))
        cursor = connection.cursor()
        cursor.execute(insertNewScorecards(**scorecardParams))
        return (JsonResponse({"Status": "Saved"}))
    except Exception as err:
        print(str(err))
        return JsonResponse({"Status": "Error", "Error": str(err)})

# Area
def stratAreaView(request):
    form = stratAreaForm()
    return render(request, 'themes/area.html' ,{'form':form})

def areaJsonList(request):
    with connection.cursor() as cursor:
            cursor.execute(fetchArea())
            rows = cursor.fetchall()
            
    tempRes = None
    jsonResultData = []

    for row in rows:
        tempRes = {
            'areaId': row[0],
            'code': row[1],
            'name':row[2],
            'isActive': row[3]
        }
        jsonResultData.append(tempRes)
    return JsonResponse({"data":list(jsonResultData)}, safe=False)

def areaSaveParams(request):
    cursor = connection.cursor()
    if(request.POST):
        form = stratAreaForm(request.POST)
        try:
            if form.is_valid():
                stratAreaParams['code'] = form['code'].value()
                stratAreaParams['name'] = form['name'].value()
                stratAreaParams['isActive'] = 'Y'
                print("Debug: " + insertNewArea(**stratAreaParams))
                form = stratAreaForm()
                cursor.execute(insertNewArea(**stratAreaParams))
                return (JsonResponse({"Status": "Saved"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

def areaUpdateParams(request,id):
    cursor = connection.cursor()
    if(request.POST):
        form = stratAreaForm(request.POST)
        try:
            if form.is_valid():
                stratAreaParams['areaId'] = id
                stratAreaParams['code'] =form['code'].value()
                stratAreaParams['name'] =form['name'].value()
                stratAreaParams['isActive'] = 'Y'
                print("Debug: " + updateArea(**stratAreaParams))
                form = stratAreaForm()
                cursor.execute(updateArea(**stratAreaParams))
                return (JsonResponse({"Status": "Updated"}))
            else:
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

@csrf_exempt        
def areaDeleteParams(request,id):
    cursor = connection.cursor()
    try:
        stratAreaParams["areaId"] = id
        stratAreaParams["isActive"] = 'N'
        print("Debug: " + deleteArea(**stratAreaParams))
        cursor.execute(deleteArea(**stratAreaParams))
        return JsonResponse({"Status":"Deleted"})
    except Exception as err:
        print(f"{type(err).__name__} was raised: {err}")
        return JsonResponse ({"Error":err}) 

#objective
def stratObjView(request):
    form = stratObjForm()
    areaList = stratArea.objects.raw(fetchArea())
    return render(request, 'themes/objective.html' ,{'form':form, 'areaList':areaList})

def objJsonList(request):
    with connection.cursor() as cursor:
            cursor.execute(fetchObj())
            rows = cursor.fetchall()
            
    tempRes = None
    jsonResultData = []

    for row in rows:
        tempRes = {
            'objId': row[0],
            'areaId':row[1],
            'area': row[2],
            'code':row[3],
            'description':row[4],
            'isActive': row[5],
           
        }
        jsonResultData.append(tempRes)
    return JsonResponse({"data":list(jsonResultData)}, safe=False)

def objSaveParams(request):
    cursor = connection.cursor()
    if(request.POST):
        form = stratObjForm(request.POST)
        try:
            if form.is_valid():
                stratObjParams['areaId'] =  request.POST['areaId']
                stratObjParams['code'] = form['code'].value()
                stratObjParams['description'] = form['description'].value()
                stratObjParams['isActive'] = 'Y'
                print("Debug: " + insertNewObj(**stratObjParams))
                form = stratObjForm()
                cursor.execute(insertNewObj(**stratObjParams))
                return (JsonResponse({"Status": "Saved"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

def objUpdateParams(request,id):
    cursor = connection.cursor()
    if(request.POST):
        form = stratObjForm(request.POST)
        try:
            if form.is_valid():
                stratObjParams['objId'] = id
                stratObjParams['areaId'] =  request.POST['areaId']
                stratObjParams['code'] =form['code'].value()
                stratObjParams['description'] =form['description'].value()
                stratObjParams['isActive'] = 'Y'
                print("Debug: " + updateObj(**stratObjParams))
                form = stratObjForm()
                cursor.execute(updateObj(**stratObjParams))
                return (JsonResponse({"Status": "Updated"}))
            else:
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

@csrf_exempt        
def ObjDeleteParams(request,id):
    cursor = connection.cursor()
    try:
        stratObjParams["objId"] = id
        stratObjParams["isActive"] = 'N'
        print("Debug: " + deleteObj(**stratObjParams))
        cursor.execute(deleteObj(**stratObjParams))
        return JsonResponse({"Status":"Deleted"})
    except Exception as err:
        print(f"{type(err).__name__} was raised: {err}")
        return JsonResponse ({"Error":err}) 

#Indicator
def stratIndView(request):
    form = stratIndForm()
    objList = stratObjective.objects.raw(fetchObj())
    typeList = refType.objects.raw(fetchType())
    return render(request, 'themes/indicator.html' ,{'form':form, 'objList':objList, 'typeList':typeList})

def indJsonList(request):
    with connection.cursor() as cursor:
            cursor.execute(fetchInd())
            rows = cursor.fetchall()
            
    tempRes = None
    jsonResultData = []

    for row in rows:
        tempRes = {
            'indId': row[0],
            'objId': row[1],
            'obj': row[2],
            'refType':row[3],
            'code':row[4],
            'description':row[5],
            'isActive': row[6]
        }
        jsonResultData.append(tempRes)
    return JsonResponse({"data":list(jsonResultData)}, safe=False)

def indSaveParams(request):
    cursor = connection.cursor()
    form = stratIndForm()
    if(request.POST):
        form = stratIndForm(request.POST)
        try:
            if form.is_valid():
                stratIndParams['objId'] = request.POST['objId']
                stratIndParams['typeNo'] = request.POST['typeNo']
                stratIndParams['code'] = form['code'].value()
                stratIndParams['description'] = form['description'].value()
                stratIndParams['isActive'] = 'Y'
                print("Debug: " + insertNewInd(**stratIndParams))
                cursor.execute(insertNewInd(**stratIndParams))
                return (JsonResponse({"Status": "Saved"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

def indUpdateParams(request,id):
    cursor = connection.cursor()
    if(request.POST):
        form = stratIndForm(request.POST)
        try:
            if form.is_valid():
                stratIndParams['indId'] = id
                stratIndParams['objId'] = request.POST['objId']
                stratIndParams['typeNo'] = request.POST['typeNo']
                stratIndParams['code'] =form['code'].value()
                stratIndParams['description'] =form['description'].value()
                stratIndParams['isActive'] = 'Y'
                print("Debug: " + updateInd(**stratIndParams))
                form = stratIndForm()
                cursor.execute(updateInd(**stratIndParams))
                return (JsonResponse({"Status": "Updated"}))
            else:
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

@csrf_exempt        
def indDeleteParams(request,id):
    cursor = connection.cursor()
    try:
        stratIndParams["indId"] = id
        stratIndParams["isActive"] = 'N'
        print("Debug: " + deleteInd(**stratIndParams))
        cursor.execute(deleteInd(**stratIndParams))
        return JsonResponse({"Status":"Deleted"})
    except Exception as err:
        print(f"{type(err).__name__} was raised: {err}")
        return JsonResponse ({"Error":err}) 


#template 
def stratTemplateListView(request):
    return render(request, 'themes/strat-template-list.html')

def tempJsonList(request):
    with connection.cursor() as cursor:
            cursor.execute(fetchTemplate())
            rows = cursor.fetchall()
            
    tempRes = None
    jsonResultData = []

    for row in rows:
        tempRes = {
            'tempId': row[0],
            'tempName': row[1],
            'createdBy':row[2],
            'createdDate': row[3],
            'isActive': row[4]
        }
        jsonResultData.append(tempRes)
    return JsonResponse({"data":list(jsonResultData)}, safe=False)


def stratTemplateView(request):
    form = stratTempForm()
    areaList = stratArea.objects.raw(fetchArea())
    return render(request, 'themes/strat-template.html',{'form':form,'areaList':areaList})

def stratRawJsonList(request):
    with connection.cursor() as cursor:
        cursor.execute(rawStratItems())
        rows = cursor.fetchall()

    areas = {}
    objects_map = {}
    indicators_map = {}

    for row in rows:
        area_id = row[0]
        if area_id not in areas:
            areas[area_id] = {
                "areaId": row[0],
                "code": row[1],
                "area": row[2],
                "isActive": row[3],
                "objects": []
            }

        obj_id = row[4]
        if obj_id:
            if obj_id not in objects_map:
                obj = {
                    "sAreaId": row[0],
                    "objId": row[4],
                    "objCode": row[5],
                    "ObjName": row[6],
                    "isActive": row[7],
                    "indicator": []
                }
                areas[area_id]["objects"].append(obj)
                objects_map[obj_id] = obj
            else:
                obj = objects_map[obj_id]

            ind_id = row[8]
            if ind_id and ind_id not in indicators_map:
                ind = {
                    "objId": row[4],
                    "indId": row[8],
                    "refType": row[9],
                    "indCode": row[10],
                    "indDesc": row[11],
                    "isActive": row[12]
                }
                obj["indicator"].append(ind)
                indicators_map[ind_id] = ind

    data = list(areas.values())
    return JsonResponse({"data": data}, json_dumps_params={'indent': 2})

def stratTempJsonList(request,id):
    with connection.cursor() as cursor:
        stratTempDetParams['tempId'] = id
        stratTempDetParams['isActive']= 'Y'
        cursor.execute(tempStratItems(**stratTempDetParams))
        rows = cursor.fetchall()

    areas = {}
    objects_map = {}
    indicators_map = {}

    for row in rows:
        area_id = row[0]
        if area_id not in areas:
            areas[area_id] = {
                "areaId": row[0],
                "code": row[1],
                "area": row[2],
                "isActive": row[3],
                "objects": []
            }

        obj_id = row[4]
        if obj_id:
            if obj_id not in objects_map:
                obj = {
                    "sAreaId": row[0],
                    "objId": row[4],
                    "objCode": row[5],
                    "ObjName": row[6],
                    "isActive": row[7],
                    "indicator": []
                }
                areas[area_id]["objects"].append(obj)
                objects_map[obj_id] = obj
            else:
                obj = objects_map[obj_id]

            ind_id = row[8]
            if ind_id and ind_id not in indicators_map:
                ind = {
                    "objId": row[4],
                    "indId": row[8],
                    "refType": row[9],
                    "indCode": row[10],
                    "indDesc": row[11],
                    "reference": row[12],
                    "target": row[13],
                    "isActive": row[14],
                    "ctrlNo":row[15]
                }
                obj["indicator"].append(ind)
                indicators_map[ind_id] = ind

    data = list(areas.values())
    return JsonResponse({"data": data}, json_dumps_params={'indent': 2})



@csrf_exempt    
def saveTemplateParams(request):
    cursor = connection.cursor()
    if request.method == 'POST':
        try:
            # Parse JSON data from the request body
            data = json.loads(request.body)
            tableData = data.get('tableData', [])
            tempId = data.get('tempId', '')

            stratTempParams['tempId'] = tempId
            stratTempParams['createdBy'] = 'admin'
            stratTempParams['tempName']= data.get('tempName', '')
            stratTempParams['isActive'] = 'Y'

            cursor.execute(insertStratTemp(**stratTempParams))
            
            # saving it items from table
            for row in tableData:
                stratTempDetParams['tempId'] = tempId
                stratTempDetParams['indId'] = row.get('indId')
                stratTempDetParams['reference']  = row.get('reference')
                stratTempDetParams['target']  = row.get('target')
                stratTempDetParams['isActive']  = 'Y'
                
                cursor.execute(insertStratTempDet(**stratTempDetParams))
                # Replace with your actual query
                # insert_query = """
                # INSERT INTO your_table_name (indId, description, obj, area, tempId, tempName)
                # VALUES (%s, %s, %s, %s, %s, %s)
                # """
                # cursor.execute(insert_query, [ind_id, description, obj, area, temp_id, temp_name])
            
            connection.commit()
            return JsonResponse({"Status": "Saved"})

        except json.JSONDecodeError:
            return JsonResponse({"Status": "Error", "Message": "Invalid JSON"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse({"Status": "Error", "Message": str(err)})
    else:
        return JsonResponse({"Status": "Error", "Message": "Wrong Request Method"})
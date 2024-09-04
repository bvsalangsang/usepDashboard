from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import *
from .sqlparams import *
from .sqlcommands import *


#---------------------------------------------------------
# Dashboard
#---------------------------------------------------------
def anaDashboardView(request):
    return render(request,'themes/dashboard-analytic.html')


#---------------------------------------------------------
# Analytics
#---------------------------------------------------------
def getAnalytic(request,id):
    with connection.cursor() as cursor:
            analIndParams['analId'] = id
            cursor.execute(getAnalInd(**analIndParams))
            rows = cursor.fetchall()
            
    tempRes = None
    jsonResultData = []

    for row in rows:
        tempRes = {
            'analId': row[0],
            'program': row[1],
            'type':row[2],
            'indicator': row[3],
            'isActive': row[4]
        }
        jsonResultData.append(tempRes)
    return JsonResponse({"data":jsonResultData}, safe=False)

def analyticsView(request):
    form = analyticsForm()
    resultType = refType.objects.raw(fetchType())
    resultAnalProg = analPrograms.objects.raw(fetchAnalProg())
    return render(request,'themes/analytics.html', {'aform':form, 'types':resultType, 'programs':resultAnalProg})

def analJsonList(request):
    with connection.cursor() as cursor:
            cursor.execute(fetchAnalytics())
            rows = cursor.fetchall()
            
    tempRes = None
    jsonResultData = []

    for row in rows:
        tempRes = {
            'analId': row[0],
            'program': row[1],
            'type':row[2],
            'indicator': row[3],
            'isActive': row[4]
        }
        jsonResultData.append(tempRes)
    return JsonResponse({"data":list(jsonResultData)}, safe=False)

def analSaveParams(request):
    cursor = connection.cursor()
    if(request.POST):
        form = analyticsForm(request.POST)
        try:
            if form.is_valid():
                analyticsParams['progId'] =request.POST['progId']
                analyticsParams['typeNo'] = request.POST['typeNo']
                analyticsParams['indicator'] = form['indicator'].value()
                analyticsParams['isActive'] = 'Y'
                print("Debug: " + insertNewAnal(**analyticsParams))
                form = analyticsForm()
                cursor.execute(insertNewAnal(**analyticsParams))
                return (JsonResponse({"Status": "Saved"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

def analUpdateParams(request,id):
    cursor = connection.cursor()
    if(request.POST):
        form = analyticsForm(request.POST)
        try:
            if form.is_valid():
                analyticsParams['analId'] = id
                analyticsParams['progId'] =request.POST['progId']
                analyticsParams['typeNo'] = request.POST['typeNo']
                analyticsParams['indicator'] = form['indicator'].value()
                analyticsParams['isActive'] = 'Y'
                print("Debug: " + updateAnal(**analyticsParams))
                form = analyticsForm()
                cursor.execute(updateAnal(**analyticsParams))
                return (JsonResponse({"Status": "Updated"}))
            else:
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

@csrf_exempt        
def analDeleteParams(request,id):
    cursor = connection.cursor()
    try:
        analyticsParams["analId"] = id
        analyticsParams["isActive"] = 'N'
        print("Debug: " + deleteAnal(**analyticsParams))
        cursor.execute(deleteAnal(**analyticsParams))
        return JsonResponse({"Status":"Deleted"})
    except Exception as err:
        print(f"{type(err).__name__} was raised: {err}")
        return JsonResponse ({"Error":err}) 

#---------------------------------------------------------
# Indicator - board passer
#---------------------------------------------------------
def boardPassersView(request):
    form = analBPForm()
    resultAnal = analytics.objects.raw(fetchAnalytics())
    return render(request,'themes/boardpassers.html',{'form':form,'indicators':resultAnal})

def boardPasserJsonList(request):
    with connection.cursor() as cursor:
            cursor.execute(fetchBoardPasser())
            rows = cursor.fetchall()
            
    tempRes = None
    jsonResultData = []

    for row in rows:
        tempRes = {
            'ctrlNo': row[0],
            'analId': row[1],
            'indicator': row[2],
            'year':row[3],
            'noOfTakers': row[4],
            'noOfPassers':row[5],
            'percentage': row[6],
            'isActive': row[7]
        }
        jsonResultData.append(tempRes)
    return JsonResponse({"data":list(jsonResultData)}, safe=False)

def boardPasserSaveParams(request):
    cursor = connection.cursor()
    if(request.POST):
        form = analBPForm(request.POST)
        try:
            if form.is_valid():
                boardPasserParams['analId'] = request.POST['analId']
                boardPasserParams['year'] = request.POST['year']
                boardPasserParams['noOfTakers'] = request.POST['noOfTakers']
                boardPasserParams['noOfPassers'] = request.POST['noOfPassers']
                boardPasserParams['percentage'] = request.POST['percentage']
                boardPasserParams['isActive'] = 'Y'
                print("Debug: " + insertNewBoardPasser(**boardPasserParams))
                form = analBPForm()
                cursor.execute(insertNewBoardPasser(**boardPasserParams))
                return (JsonResponse({"Status": "Saved"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

def boardPasserUpdateParams(request, id):
    cursor = connection.cursor()
    if(request.POST):
        form = analBPForm(request.POST)
        try:
            if form.is_valid():
          
                boardPasserParams['ctrlNo'] = id
                boardPasserParams['analId'] = request.POST['analId']
                boardPasserParams['year'] = request.POST['year']
                boardPasserParams['noOfTakers'] = request.POST['noOfTakers']
                boardPasserParams['noOfPassers'] = request.POST['noOfPassers']
                boardPasserParams['percentage'] = request.POST['percentage']
                boardPasserParams['isActive'] = 'Y'
                print("Debug: " + updateBoardpasser(**boardPasserParams))
                form = analBPForm()
                cursor.execute(updateBoardpasser(**boardPasserParams))
                return (JsonResponse({"Status": "Updated"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

@csrf_exempt  
def boardPasserDeleteParams(request, id):
    cursor = connection.cursor()
    try:
        boardPasserParams['ctrlNo'] = id
        boardPasserParams['isActive'] = 'N'
        print("Debug: " + deleteBoardPasser(**boardPasserParams))
        cursor.execute(deleteBoardPasser(**boardPasserParams))
        return (JsonResponse({"Status": "Deleted"}))
    except Exception as err:
        print(f"{type(err).__name__} was raised: {err}")
        return JsonResponse ({"err":err})
    
#---------------------------------------------------------
# Indicator - employabilitily
#---------------------------------------------------------
def employabilityView(request):
    form = analEmployForm()
    return render(request,'themes/employability.html',{'form':form})

def employabilityJsonList(request):
    with connection.cursor() as cursor:
            cursor.execute(fetchEmployability())
            rows = cursor.fetchall()
            
    tempRes = None
    jsonResultData = []

    for row in rows:
        tempRes = {
            'ctrlNo': row[0],
            'analId': row[1],
            'indicator': row[2],
            'year':row[3],
            'noOfGrads': row[4],
            'noOfEmployed':row[5],
            'percentage': row[6],
            'isActive': row[7]
        }
        jsonResultData.append(tempRes)
    return JsonResponse({"data":list(jsonResultData)}, safe=False)

def employabilitySaveParams(request):
    cursor = connection.cursor()
    if(request.POST):
        form = analEmployForm(request.POST)
        try:
            if form.is_valid():
                employabilityParams['analId'] = request.POST['analId']
                employabilityParams['year'] = request.POST['year']
                employabilityParams['noOfGrads'] = request.POST['noOfGrads']
                employabilityParams['noOfEmployed'] = request.POST['noOfEmployed']
                employabilityParams['percentage'] = request.POST['percentage']
                employabilityParams['isActive'] = 'Y'
                print("Debug: " + insertNewEmployability(**employabilityParams))
                form = analEmployForm()
                cursor.execute(insertNewEmployability(**employabilityParams))
                return (JsonResponse({"Status": "Saved"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

def employabilityUpdateParams(request, id):
    cursor = connection.cursor()
    if(request.POST):
        form = analEmployForm(request.POST)
        try:
            if form.is_valid():
          
                employabilityParams['ctrlNo'] = id
                employabilityParams['analId'] = request.POST['analId']
                employabilityParams['year'] = request.POST['year']
                employabilityParams['noOfGrads'] = request.POST['noOfGrads']
                employabilityParams['noOfEmployed'] = request.POST['noOfEmployed']
                employabilityParams['percentage'] = request.POST['percentage']
                employabilityParams['isActive'] = 'Y'
                print("Debug: " + updateEmployability(**employabilityParams))
                form = analEmployForm()
                cursor.execute(updateEmployability(**employabilityParams))
                return (JsonResponse({"Status": "Updated"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

@csrf_exempt  
def employabilityDeleteParams(request, id):
    cursor = connection.cursor()
    try:
        employabilityParams['ctrlNo'] = id
        employabilityParams['isActive'] = 'N'
        print("Debug: " + deleteEmployability(**employabilityParams))
        cursor.execute(deleteEmployability(**employabilityParams))
        return (JsonResponse({"Status": "Deleted"}))
    except Exception as err:
        print(f"{type(err).__name__} was raised: {err}")
        return JsonResponse ({"err":err})
    
#---------------------------------------------------------
# Indicator - CHED and RDC identified
#---------------------------------------------------------
def chedRdcView(request):
    form = analChedRdcForm()
    return render(request,'themes/chedrdcident.html',{'form':form})

def chedRdcJsonList(request):
    with connection.cursor() as cursor:
            cursor.execute(fetchChedRdcIdent())
            rows = cursor.fetchall()
            
    tempRes = None
    jsonResultData = []

    for row in rows:
        tempRes = {
            'ctrlNo': row[0],
            'analId': row[1],
            'indicator': row[2],
            'year':row[3],
            'noOfUnderGrad': row[4],
            'noOfChedRdcIdent':row[5],
            'percentage': row[6],
            'isActive': row[7]
        }
        jsonResultData.append(tempRes)
    return JsonResponse({"data":list(jsonResultData)}, safe=False)

def chedRdcSaveParams(request):
    cursor = connection.cursor()
    if(request.POST):
        form = analChedRdcForm(request.POST)
        try:
            if form.is_valid():
                chedRdcParams['analId'] = request.POST['analId']
                chedRdcParams['year'] = request.POST['year']
                chedRdcParams['noOfUnderGrad'] = request.POST['noOfUnderGrad']
                chedRdcParams['noOfChedRdcIdent'] = request.POST['noOfChedRdcIdent']
                chedRdcParams['percentage'] = request.POST['percentage']
                chedRdcParams['isActive'] = 'Y'
                print("Debug: " + insertNewChedRdcIdent(**chedRdcParams))
                form = analChedRdcForm()
                cursor.execute(insertNewChedRdcIdent(**chedRdcParams))
                return (JsonResponse({"Status": "Saved"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

def chedRdcUpdateParams(request, id):
    cursor = connection.cursor()
    if(request.POST):
        form = analChedRdcForm(request.POST)
        try:
            if form.is_valid():
          
                chedRdcParams['ctrlNo'] = id
                chedRdcParams['analId'] = request.POST['analId']
                chedRdcParams['year'] = request.POST['year']
                chedRdcParams['noOfUnderGrad'] = request.POST['noOfUnderGrad']
                chedRdcParams['noOfChedRdcIdent'] = request.POST['noOfChedRdcIdent']
                chedRdcParams['percentage'] = request.POST['percentage']
                chedRdcParams['isActive'] = 'Y'
                print("Debug: " + updateChedRdcIdent(**chedRdcParams))
                form = analChedRdcForm()
                cursor.execute(updateChedRdcIdent(**chedRdcParams))
                return (JsonResponse({"Status": "Updated"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

@csrf_exempt  
def chedRdcDeleteParams(request, id):
    cursor = connection.cursor()
    try:
        chedRdcParams['ctrlNo'] = id
        chedRdcParams['isActive'] = 'N'
        print("Debug: " + deleteChedRdcIdent(**chedRdcParams))
        cursor.execute(deleteChedRdcIdent(**chedRdcParams))
        return (JsonResponse({"Status": "Deleted"}))
    except Exception as err:
        print(f"{type(err).__name__} was raised: {err}")
        return JsonResponse ({"err":err})
    
#---------------------------------------------------------
# Indicator - Accreditation
#---------------------------------------------------------
def accredView(request):
    form = analAccredForm()
    return render(request,'themes/accreditation.html',{'form':form})

def accredJsonList(request):
    with connection.cursor() as cursor:
            cursor.execute(fetchAccred())
            rows = cursor.fetchall()
            
    tempRes = None
    jsonResultData = []

    for row in rows:
        tempRes = {
            'ctrlNo': row[0],
            'analId': row[1],
            'indicator': row[2],
            'year':row[3],
            'noOfUnderGradProg': row[4],
            'noOfUnderGradProgAccred':row[5],
            'percentage': row[6],
            'isActive': row[7]
        }
        jsonResultData.append(tempRes)
    return JsonResponse({"data":list(jsonResultData)}, safe=False)

def accredSaveParams(request):
    cursor = connection.cursor()
    if(request.POST):
        form = analAccredForm(request.POST)
        try:
            if form.is_valid():
                accredParams['analId'] = request.POST['analId']
                accredParams['year'] = request.POST['year']
                accredParams['noOfUnderGradProg'] = request.POST['noOfUnderGradProg']
                accredParams['noOfUnderGradProgAccred'] = request.POST['noOfUnderGradProgAccred']
                accredParams['percentage'] = request.POST['percentage']
                accredParams['isActive'] = 'Y'
                print("Debug: " + insertNewAccred(**accredParams))
                form = analAccredForm()
                cursor.execute(insertNewAccred(**accredParams))
                return (JsonResponse({"Status": "Saved"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

def accredUpdateParams(request, id):
    cursor = connection.cursor()
    if(request.POST):
        form = analAccredForm(request.POST)
        try:
            if form.is_valid():
          
                accredParams['ctrlNo'] = id
                accredParams['analId'] = request.POST['analId']
                accredParams['year'] = request.POST['year']
                accredParams['noOfUnderGradProg'] = request.POST['noOfUnderGradProg']
                accredParams['noOfUnderGradProgAccred'] = request.POST['noOfUnderGradProgAccred']
                accredParams['percentage'] = request.POST['percentage']
                accredParams['isActive'] = 'Y'
                print("Debug: " + updateAccred(**accredParams))
                form = analAccredForm()
                cursor.execute(updateAccred(**accredParams))
                return (JsonResponse({"Status": "Updated"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

@csrf_exempt  
def accredDeleteParams(request, id):
    cursor = connection.cursor()
    try:
        accredParams['ctrlNo'] = id
        accredParams['isActive'] = 'N'
        print("Debug: " + deleteAccred(**accredParams))
        cursor.execute(deleteAccred(**accredParams))
        return (JsonResponse({"Status": "Deleted"}))
    except Exception as err:
        print(f"{type(err).__name__} was raised: {err}")
        return JsonResponse ({"err":err})
    
#---------------------------------------------------------
# Indicator - Graduate School Faculty (Research Work)
#---------------------------------------------------------
def gradResView(request):
    form = analGradResForm()
    return render(request,'themes/gradres.html',{'form':form})

def gradResJsonList(request):
    with connection.cursor() as cursor:
            cursor.execute(fetchGradRes())
            rows = cursor.fetchall()
            
    tempRes = None
    jsonResultData = []

    for row in rows:
        tempRes = {
            'ctrlNo': row[0],
            'analId': row[1],
            'indicator': row[2],
            'year':row[3],
            'noOfGradFac': row[4],
            'noOfGradFacRes':row[5],
            'percentage': row[6],
            'isActive': row[7]
        }
        jsonResultData.append(tempRes)
    return JsonResponse({"data":list(jsonResultData)}, safe=False)

def gradResSaveParams(request):
    cursor = connection.cursor()
    if(request.POST):
        form = analGradResForm(request.POST)
        try:
            if form.is_valid():
                gradresParams['analId'] = request.POST['analId']
                gradresParams['year'] = request.POST['year']
                gradresParams['noOfGradFac'] = request.POST['noOfGradFac']
                gradresParams['noOfGradFacRes'] = request.POST['noOfGradFacRes']
                gradresParams['percentage'] = request.POST['percentage']
                gradresParams['isActive'] = 'Y'
                print("Debug: " + insertNewGradRes(**gradresParams))
                form = analGradResForm()
                cursor.execute(insertNewGradRes(**gradresParams))
                return (JsonResponse({"Status": "Saved"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

def gradResUpdateParams(request, id):
    cursor = connection.cursor()
    if(request.POST):
        form = analGradResForm(request.POST)
        try:
            if form.is_valid():
                gradresParams['ctrlNo'] = id
                gradresParams['analId'] = request.POST['analId']
                gradresParams['year'] = request.POST['year']
                gradresParams['noOfGradFac'] = request.POST['noOfGradFac']
                gradresParams['noOfGradFacRes'] = request.POST['noOfGradFacRes']
                gradresParams['percentage'] = request.POST['percentage']
                gradresParams['isActive'] = 'Y'
                print("Debug: " + updateGradRes(**gradresParams))
                form = analGradResForm()
                cursor.execute(updateGradRes(**gradresParams))
                return (JsonResponse({"Status": "Updated"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

@csrf_exempt  
def gradResDeleteParams(request, id):
    cursor = connection.cursor()
    try:
        gradresParams['ctrlNo'] = id
        gradresParams['isActive'] = 'N'
        print("Debug: " + deleteGradRes(**gradresParams))
        cursor.execute(deleteGradRes(**gradresParams))
        return (JsonResponse({"Status": "Deleted"}))
    except Exception as err:
        print(f"{type(err).__name__} was raised: {err}")
        return JsonResponse ({"err":err})
    
#---------------------------------------------------------
# Indicator - Research Degree
#---------------------------------------------------------
def resDegView(request):
    form = analResDegForm()
    return render(request,'themes/researchdeg.html',{'form':form})

def resDegJsonList(request):
    with connection.cursor() as cursor:
            cursor.execute(fetchResDeg())
            rows = cursor.fetchall()
            
    tempRes = None
    jsonResultData = []

    for row in rows:
        tempRes = {
            'ctrlNo': row[0],
            'analId': row[1],
            'indicator': row[2],
            'year':row[3],
            'noOfGrad': row[4],
            'noOfGradResDeg':row[5],
            'percentage': row[6],
            'isActive': row[7]
        }
        jsonResultData.append(tempRes)
    return JsonResponse({"data":list(jsonResultData)}, safe=False)

def resDegSaveParams(request):
    cursor = connection.cursor()
    if(request.POST):
        form = analResDegForm(request.POST)
        try:
            if form.is_valid():
                resDegParams['analId'] = request.POST['analId']
                resDegParams['year'] = request.POST['year']
                resDegParams['noOfGrad'] = request.POST['noOfGrad']
                resDegParams['noOfGradResDeg'] = request.POST['noOfGradResDeg']
                resDegParams['percentage'] = request.POST['percentage']
                resDegParams['isActive'] = 'Y'
                print("Debug: " + insertNewResDeg(**resDegParams))
                form = analResDegForm()
                cursor.execute(insertNewResDeg(**resDegParams))
                return (JsonResponse({"Status": "Saved"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

def resDegUpdateParams(request, id):
    cursor = connection.cursor()
    if(request.POST):
        form = analResDegForm(request.POST)
        try:
            if form.is_valid():
                resDegParams['ctrlNo'] = id
                resDegParams['analId'] = request.POST['analId']
                resDegParams['year'] = request.POST['year']
                resDegParams['noOfGrad'] = request.POST['noOfGrad']
                resDegParams['noOfGradResDeg'] = request.POST['noOfGradResDeg']
                resDegParams['percentage'] = request.POST['percentage']
                resDegParams['isActive'] = 'Y'
                print("Debug: " + updateResDeg(**resDegParams))
                form = analResDegForm()
                cursor.execute(updateResDeg(**resDegParams))
                return (JsonResponse({"Status": "Updated"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

@csrf_exempt  
def resDegDeleteParams(request, id):
    cursor = connection.cursor()
    try:
        resDegParams['ctrlNo'] = id
        resDegParams['isActive'] = 'N'
        print("Debug: " + deleteResDeg(**resDegParams))
        cursor.execute(deleteResDeg(**resDegParams))
        return (JsonResponse({"Status": "Deleted"}))
    except Exception as err:
        print(f"{type(err).__name__} was raised: {err}")
        return JsonResponse ({"err":err})
    
#---------------------------------------------------------
# Indicator - Accredited Graduate Programs
#---------------------------------------------------------
def accrGradProgView(request):
    form = analAccrGradProgForm()
    return render(request,'themes/accrgradprog.html',{'form':form})

def accrGradProgJsonList(request):
    with connection.cursor() as cursor:
            cursor.execute(fetchAccGradProg())
            rows = cursor.fetchall()
            
    tempRes = None
    jsonResultData = []

    for row in rows:
        tempRes = {
            'ctrlNo': row[0],
            'analId': row[1],
            'indicator': row[2],
            'year':row[3],
            'noOfGradProg': row[4],
            'noOfAccrGradProg':row[5],
            'percentage': row[6],
            'isActive': row[7]
        }
        jsonResultData.append(tempRes)
    return JsonResponse({"data":list(jsonResultData)}, safe=False)

def accrGradProgSaveParams(request):
    cursor = connection.cursor()
    if(request.POST):
        form = analAccrGradProgForm(request.POST)
        try:
            if form.is_valid():
                accrGradProgParams['analId'] = request.POST['analId']
                accrGradProgParams['year'] = request.POST['year']
                accrGradProgParams['noOfGradProg'] = request.POST['noOfGradProg']
                accrGradProgParams['noOfAccrGradProg'] = request.POST['noOfAccrGradProg']
                accrGradProgParams['percentage'] = request.POST['percentage']
                accrGradProgParams['isActive'] = 'Y'
                print("Debug: " + insertNewAccrGradProg(**accrGradProgParams))
                form = analAccrGradProgForm()
                cursor.execute(insertNewAccrGradProg(**accrGradProgParams))
                return (JsonResponse({"Status": "Saved"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

def accrGradProgUpdateParams(request, id):
    cursor = connection.cursor()
    if(request.POST):
        form = analAccrGradProgForm(request.POST)
        try:
            if form.is_valid():
                accrGradProgParams['ctrlNo'] = id
                accrGradProgParams['analId'] = request.POST['analId']
                accrGradProgParams['year'] = request.POST['year']
                accrGradProgParams['noOfGradProg'] = request.POST['noOfGradProg']
                accrGradProgParams['noOfAccrGradProg'] = request.POST['noOfAccrGradProg']
                accrGradProgParams['percentage'] = request.POST['percentage']
                accrGradProgParams['isActive'] = 'Y'
                print("Debug: " + updateAccrGradProg(**accrGradProgParams))
                form = analAccrGradProgForm()
                cursor.execute(updateAccrGradProg(**accrGradProgParams))
                return (JsonResponse({"Status": "Updated"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

@csrf_exempt  
def accrGradProgDeleteParams(request, id):
    cursor = connection.cursor()
    try:
        accrGradProgParams['ctrlNo'] = id
        accrGradProgParams['isActive'] = 'N'
        print("Debug: " + deleteAccrGradProg(**accrGradProgParams))
        cursor.execute(deleteAccrGradProg(**accrGradProgParams))
        return (JsonResponse({"Status": "Deleted"}))
    except Exception as err:
        print(f"{type(err).__name__} was raised: {err}")
        return JsonResponse ({"err":err})
    
#---------------------------------------------------------
# Indicator - Research output
#---------------------------------------------------------
def resOutputView(request):
    form = analResOutputForm()
    return render(request,'themes/resoutput.html',{'form':form})

def resOutputJsonList(request):
    with connection.cursor() as cursor:
            cursor.execute(fetchResOutput())
            rows = cursor.fetchall()
            
    tempRes = None
    jsonResultData = []

    for row in rows:
        tempRes = {
            'ctrlNo': row[0],
            'analId': row[1],
            'indicator': row[2],
            'year':row[3],
            'noOfResOutput': row[4],
            'isActive': row[5]
        }
        jsonResultData.append(tempRes)
    return JsonResponse({"data":list(jsonResultData)}, safe=False)

def resOutputSaveParams(request):
    cursor = connection.cursor()
    if(request.POST):
        form = analResOutputForm(request.POST)
        try:
            if form.is_valid():
                resOutputParams['analId'] = request.POST['analId']
                resOutputParams['year'] = request.POST['year']
                resOutputParams['noOfResOutput'] = request.POST['noOfResOutput']
                resOutputParams['isActive'] = 'Y'
                print("Debug: " + insertNewResOutput(**resOutputParams))
                form = analResOutputForm()
                cursor.execute(insertNewResOutput(**resOutputParams))
                return (JsonResponse({"Status": "Saved"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

def resOutputUpdateParams(request, id):
    cursor = connection.cursor()
    if(request.POST):
        form = analResOutputForm(request.POST)
        try:
            if form.is_valid():
                resOutputParams['ctrlNo'] = id
                resOutputParams['analId'] = request.POST['analId']
                resOutputParams['year'] = request.POST['year']
                resOutputParams['noOfResOutput'] = request.POST['noOfResOutput']
                resOutputParams['isActive'] = 'Y'
                print("Debug: " + updateResOutput(**resOutputParams))
                form = analResOutputForm()
                cursor.execute(updateResOutput(**resOutputParams))
                return (JsonResponse({"Status": "Updated"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

@csrf_exempt  
def resOutputDeleteParams(request, id):
    cursor = connection.cursor()
    try:
        resOutputParams['ctrlNo'] = id
        resOutputParams['isActive'] = 'N'
        print("Debug: " + deleteResOutput(**resOutputParams))
        cursor.execute(deleteResOutput(**resOutputParams))
        return (JsonResponse({"Status": "Deleted"}))
    except Exception as err:
        print(f"{type(err).__name__} was raised: {err}")
        return JsonResponse ({"err":err})
    
    
#---------------------------------------------------------
# Indicator - Research output Complete
#---------------------------------------------------------
def resCompleteView(request):
    form = analResCompleteForm()
    return render(request,'themes/resoutcomplete.html',{'form':form})

def resCompleteJsonList(request):
    with connection.cursor() as cursor:
            cursor.execute(fetchResComplete())
            rows = cursor.fetchall()
            
    tempRes = None
    jsonResultData = []

    for row in rows:
        tempRes = {
            'ctrlNo': row[0],
            'analId': row[1],
            'indicator': row[2],
            'year':row[3],
            'noOfResComplete': row[4],
            'isActive': row[5]
        }
        jsonResultData.append(tempRes)
    return JsonResponse({"data":list(jsonResultData)}, safe=False)

def resCompleteSaveParams(request):
    cursor = connection.cursor()
    if(request.POST):
        form = analResCompleteForm(request.POST)
        try:
            if form.is_valid():
                resCompleteParams['analId'] = request.POST['analId']
                resCompleteParams['year'] = request.POST['year']
                resCompleteParams['noOfResComplete'] = request.POST['noOfResComplete']
                resCompleteParams['isActive'] = 'Y'
                print("Debug: " + insertNewResOutput(**resCompleteParams))
                form = analResCompleteForm()
                cursor.execute(insertNewResOutput(**resCompleteParams))
                return (JsonResponse({"Status": "Saved"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

def resCompleteUpdateParams(request, id):
    cursor = connection.cursor()
    if(request.POST):
        form = analResCompleteForm(request.POST)
        try:
            if form.is_valid():
                resCompleteParams['ctrlNo'] = id
                resCompleteParams['analId'] = request.POST['analId']
                resCompleteParams['year'] = request.POST['year']
                resCompleteParams['noOfResComplete'] = request.POST['noOfResComplete']
                resCompleteParams['isActive'] = 'Y'
                print("Debug: " + updateResComplete(**resCompleteParams))
                form = analResCompleteForm()
                cursor.execute(updateResComplete(**resCompleteParams))
                return (JsonResponse({"Status": "Updated"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

@csrf_exempt  
def resCompleteDeleteParams(request, id):
    cursor = connection.cursor()
    try:
        resCompleteParams['ctrlNo'] = id
        resCompleteParams['isActive'] = 'N'
        print("Debug: " + deleteResComplete(**resCompleteParams))
        cursor.execute(deleteResComplete(**resCompleteParams))
        return (JsonResponse({"Status": "Deleted"}))
    except Exception as err:
        print(f"{type(err).__name__} was raised: {err}")
        return JsonResponse ({"err":err})
    
#---------------------------------------------------------
# Indicator - Research Published
#---------------------------------------------------------
def resPublishedView(request):
    form = analResPublishedForm()
    return render(request,'themes/respublished.html',{'form':form})

def resPublishedJsonList(request):
    with connection.cursor() as cursor:
            cursor.execute(fetchResPublished())
            rows = cursor.fetchall()
            
    tempRes = None
    jsonResultData = []

    for row in rows:
        tempRes = {
            'ctrlNo': row[0],
            'analId': row[1],
            'indicator': row[2],
            'year':row[3],
            'noOfResOutput': row[4],
            'noOfResPublished':row[5],
            'percentage': row[6],
            'isActive': row[7]
        }
        jsonResultData.append(tempRes)
    return JsonResponse({"data":list(jsonResultData)}, safe=False)

def resPublishedSaveParams(request):
    cursor = connection.cursor()
    if(request.POST):
        form = analResPublishedForm(request.POST)
        try:
            if form.is_valid():
                resPublishedParams['analId'] = request.POST['analId']
                resPublishedParams['year'] = request.POST['year']
                resPublishedParams['noOfResOutput'] = request.POST['noOfResOutput']
                resPublishedParams['noOfResPublished'] = request.POST['noOfResPublished']
                resPublishedParams['percentage'] = request.POST['percentage']
                resPublishedParams['isActive'] = 'Y'
                print("Debug: " + insertNewResPublished(**resPublishedParams))
                form = analResPublishedForm()
                cursor.execute(insertNewResPublished(**resPublishedParams))
                return (JsonResponse({"Status": "Saved"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

def resPublishedUpdateParams(request, id):
    cursor = connection.cursor()
    if(request.POST):
        form = analResPublishedForm(request.POST)
        try:
            if form.is_valid():
                resPublishedParams['ctrlNo'] = id
                resPublishedParams['analId'] = request.POST['analId']
                resPublishedParams['year'] = request.POST['year']
                resPublishedParams['noOfResOutput'] = request.POST['noOfResOutput']
                resPublishedParams['noOfResPublished'] = request.POST['noOfResPublished']
                resPublishedParams['percentage'] = request.POST['percentage']
                resPublishedParams['isActive'] = 'Y'
                print("Debug: " + updateResPublished(**resPublishedParams))
                form = analResPublishedForm()
                cursor.execute(updateResPublished(**resPublishedParams))
                return (JsonResponse({"Status": "Updated"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

@csrf_exempt  
def resPublishedDeleteParams(request, id):
    cursor = connection.cursor()
    try:
        resPublishedParams['ctrlNo'] = id
        resPublishedParams['isActive'] = 'N'
        print("Debug: " + deleteResPublished(**resPublishedParams))
        cursor.execute(deleteResPublished(**resPublishedParams))
        return (JsonResponse({"Status": "Deleted"}))
    except Exception as err:
        print(f"{type(err).__name__} was raised: {err}")
        return JsonResponse ({"err":err})
    
#---------------------------------------------------------
# Indicator - Active Partners
#---------------------------------------------------------
def actPartnerView(request):
    form = analActPartnerForm()
    return render(request,'themes/activepartner.html',{'form':form})

def actPartnerJsonList(request):
    with connection.cursor() as cursor:
            cursor.execute(fetchActPartner())
            rows = cursor.fetchall()
            
    tempRes = None
    jsonResultData = []

    for row in rows:
        tempRes = {
            'ctrlNo': row[0],
            'analId': row[1],
            'indicator': row[2],
            'year':row[3],
            'noOfActPart': row[4],
            'isActive': row[5]
        }
        jsonResultData.append(tempRes)
    return JsonResponse({"data":list(jsonResultData)}, safe=False)

def actPartnerSaveParams(request):
    cursor = connection.cursor()
    if(request.POST):
        form = analActPartnerForm(request.POST)
        try:
            if form.is_valid():
                actPartnerParams['analId'] = request.POST['analId']
                actPartnerParams['year'] = request.POST['year']
                actPartnerParams['noOfActPart'] = request.POST['noOfActPart']
                actPartnerParams['isActive'] = 'Y'
                print("Debug: " + insertNewActPartner(**actPartnerParams))
                form = analActPartnerForm()
                cursor.execute(insertNewActPartner(**actPartnerParams))
                return (JsonResponse({"Status": "Saved"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

def actPartnerUpdateParams(request, id):
    cursor = connection.cursor()
    if(request.POST):
        form = analActPartnerForm(request.POST)
        try:
            if form.is_valid():
                actPartnerParams['ctrlNo'] = id
                actPartnerParams['analId'] = request.POST['analId']
                actPartnerParams['year'] = request.POST['year']
                actPartnerParams['noOfActPart'] = request.POST['noOfActPart']
                actPartnerParams['isActive'] = 'Y'
                print("Debug: " + updateActPartner(**actPartnerParams))
                form = analActPartnerForm()
                cursor.execute(updateActPartner(**actPartnerParams))
                return (JsonResponse({"Status": "Updated"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

@csrf_exempt  
def actPartnerDeleteParams(request, id):
    cursor = connection.cursor()
    try:
        actPartnerParams['ctrlNo'] = id
        actPartnerParams['isActive'] = 'N'
        print("Debug: " + deleteActPartner(**actPartnerParams))
        cursor.execute(deleteActPartner(**actPartnerParams))
        return (JsonResponse({"Status": "Deleted"}))
    except Exception as err:
        print(f"{type(err).__name__} was raised: {err}")
        return JsonResponse ({"err":err})
    
#---------------------------------------------------------
# Indicator - Active Partners
#---------------------------------------------------------
def traineesView(request):
    form = analTraineesForm()
    return render(request,'themes/numtrainees.html',{'form':form})

def traineesJsonList(request):
    with connection.cursor() as cursor:
            cursor.execute(fetchTrainees())
            rows = cursor.fetchall()
            
    tempRes = None
    jsonResultData = []

    for row in rows:
        tempRes = {
            'ctrlNo': row[0],
            'analId': row[1],
            'indicator': row[2],
            'year':row[3],
            'noOfTrainees': row[4],
            'isActive': row[5]
        }
        jsonResultData.append(tempRes)
    return JsonResponse({"data":list(jsonResultData)}, safe=False)

def traineesSaveParams(request):
    cursor = connection.cursor()
    if(request.POST):
        form = analTraineesForm(request.POST)
        try:
            if form.is_valid():
                traineesParams['analId'] = request.POST['analId']
                traineesParams['year'] = request.POST['year']
                traineesParams['noOfTrainees'] = request.POST['noOfTrainees']
                traineesParams['isActive'] = 'Y'
                print("Debug: " + insertNewTrainees(**traineesParams))
                form = analTraineesForm()
                cursor.execute(insertNewTrainees(**traineesParams))
                return (JsonResponse({"Status": "Saved"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

def traineesUpdateParams(request, id):
    cursor = connection.cursor()
    if(request.POST):
        form = analTraineesForm(request.POST)
        try:
            if form.is_valid():
                traineesParams['ctrlNo'] = id
                traineesParams['analId'] = request.POST['analId']
                traineesParams['year'] = request.POST['year']
                traineesParams['noOfTrainees'] = request.POST['noOfTrainees']
                traineesParams['isActive'] = 'Y'
                print("Debug: " + updateTrainees(**traineesParams))
                form = analTraineesForm()
                cursor.execute(updateTrainees(**traineesParams))
                return (JsonResponse({"Status": "Updated"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

@csrf_exempt  
def traineesDeleteParams(request, id):
    cursor = connection.cursor()
    try:
        traineesParams['ctrlNo'] = id
        traineesParams['isActive'] = 'N'
        print("Debug: " + deleteTrainees(**traineesParams))
        cursor.execute(deleteTrainees(**traineesParams))
        return (JsonResponse({"Status": "Deleted"}))
    except Exception as err:
        print(f"{type(err).__name__} was raised: {err}")
        return JsonResponse ({"err":err})
    
#---------------------------------------------------------
# Indicator - Active Partners
#---------------------------------------------------------
def extProgramView(request):
    form = analExtProgramForm()
    return render(request,'themes/extprogram.html',{'form':form})

def extProgramJsonList(request):
    with connection.cursor() as cursor:
            cursor.execute(fetchExtProgram())
            rows = cursor.fetchall()
            
    tempRes = None
    jsonResultData = []

    for row in rows:
        tempRes = {
            'ctrlNo': row[0],
            'analId': row[1],
            'indicator': row[2],
            'year':row[3],
            'noOfExtProgram': row[4],
            'isActive': row[5]
        }
        jsonResultData.append(tempRes)
    return JsonResponse({"data":list(jsonResultData)}, safe=False)

def extProgramSaveParams(request):
    cursor = connection.cursor()
    if(request.POST):
        form = analExtProgramForm(request.POST)
        try:
            if form.is_valid():
                extProgramParams['analId'] = request.POST['analId']
                extProgramParams['year'] = request.POST['year']
                extProgramParams['noOfExtProgram'] = request.POST['noOfExtProgram']
                extProgramParams['isActive'] = 'Y'
                print("Debug: " + insertNewExtProgram(**extProgramParams))
                form = analExtProgramForm()
                cursor.execute(insertNewExtProgram(**extProgramParams))
                return (JsonResponse({"Status": "Saved"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

def extProgramUpdateParams(request, id):
    cursor = connection.cursor()
    if(request.POST):
        form = analExtProgramForm(request.POST)
        try:
            if form.is_valid():
                extProgramParams['ctrlNo'] = id
                extProgramParams['analId'] = request.POST['analId']
                extProgramParams['year'] = request.POST['year']
                extProgramParams['noOfExtProgram'] = request.POST['noOfExtProgram']
                extProgramParams['isActive'] = 'Y'
                print("Debug: " + updateExtProgram(**extProgramParams))
                form = analExtProgramForm()
                cursor.execute(updateExtProgram(**extProgramParams))
                return (JsonResponse({"Status": "Updated"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

@csrf_exempt  
def extProgramDeleteParams(request, id):
    cursor = connection.cursor()
    try:
        extProgramParams['ctrlNo'] = id
        extProgramParams['isActive'] = 'N'
        print("Debug: " + deleteExtProgram(**extProgramParams))
        cursor.execute(deleteExtProgram(**extProgramParams))
        return (JsonResponse({"Status": "Deleted"}))
    except Exception as err:
        print(f"{type(err).__name__} was raised: {err}")
        return JsonResponse ({"err":err})
    
#---------------------------------------------------------
# Indicator - Active Partners
#---------------------------------------------------------
def beneficiaryView(request):
    form = analBeneficiaryForm()
    return render(request,'themes/beneficiaries.html',{'form':form})

def beneficiaryJsonList(request):
    with connection.cursor() as cursor:
            cursor.execute(fetchBeneficiary())
            rows = cursor.fetchall()
            
    tempRes = None
    jsonResultData = []

    for row in rows:
        tempRes = {
            'ctrlNo': row[0],
            'analId': row[1],
            'indicator': row[2],
            'year':row[3],
            'noOfBenef': row[4],
            'noOfBenefRate':row[5],
            'percentage': row[6],
            'isActive': row[7]
        }
        jsonResultData.append(tempRes)
    return JsonResponse({"data":list(jsonResultData)}, safe=False)

def beneficiarySaveParams(request):
    cursor = connection.cursor()
    if(request.POST):
        form = analBeneficiaryForm(request.POST)
        try:
            if form.is_valid():
                benefParams['analId'] = request.POST['analId']
                benefParams['year'] = request.POST['year']
                benefParams['noOfBenef'] = request.POST['noOfBenef']
                benefParams['noOfBenefRate'] = request.POST['noOfBenefRate']
                benefParams['percentage'] = request.POST['percentage']
                benefParams['isActive'] = 'Y'
                print("Debug: " + insertNewBeneficiary(**benefParams))
                form = analBeneficiaryForm()
                cursor.execute(insertNewBeneficiary(**benefParams))
                return (JsonResponse({"Status": "Saved"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

def beneficiaryUpdateParams(request, id):
    cursor = connection.cursor()
    if(request.POST):
        form = analBeneficiaryForm(request.POST)
        try:
            if form.is_valid():
                benefParams['ctrlNo'] = id
                benefParams['analId'] = request.POST['analId']
                benefParams['year'] = request.POST['year']
                benefParams['noOfBenef'] = request.POST['noOfBenef']
                benefParams['noOfBenefRate'] = request.POST['noOfBenefRate']
                benefParams['percentage'] = request.POST['percentage']
                benefParams['isActive'] = 'Y'
                print("Debug: " + updateBeneficiary(**benefParams))
                form = analBeneficiaryForm()
                cursor.execute(updateBeneficiary(**benefParams))
                return (JsonResponse({"Status": "Updated"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

@csrf_exempt  
def beneficiaryDeleteParams(request, id):
    cursor = connection.cursor()
    try:
        benefParams['ctrlNo'] = id
        benefParams['isActive'] = 'N'
        print("Debug: " + deleteBeneficiary(**benefParams))
        cursor.execute(deleteBeneficiary(**benefParams))
        return (JsonResponse({"Status": "Deleted"}))
    except Exception as err:
        print(f"{type(err).__name__} was raised: {err}")
        return JsonResponse ({"err":err})
    
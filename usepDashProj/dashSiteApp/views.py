from django.shortcuts import render
from .sqlparams import * 
from .sqlcommands import *


# Create your views here.
def index(request):
    return render(request,'dashSiteApp/themes/index.html')

def commitment(request):
    return render(request,'dashSiteApp/themes/commitment.html')

def gad(request):
    return render(request,'dashSiteApp/themes/gad.html')

def analytics(request):
    return render(request,'dashSiteApp/themes/analytics.html')

def ludip(request):
    return render(request,'dashSiteApp/themes/ludip.html')


def scorecard(request):
    return render(request,'dashSiteApp/themes/scorecard.html')
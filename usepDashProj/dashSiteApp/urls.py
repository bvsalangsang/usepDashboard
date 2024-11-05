from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('commitment',views.commitment,name="commitment"),
    path('gad',views.gad,name="gad"),
    path('analytics',views.analytics,name="analytics"),
    path('ludip',views.ludip,name="ludip"),
    path('scorecard',views.scorecard,name="scorecard"),
 ]

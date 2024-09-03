from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('dashboard-ludip/',views.ludipDash,name="ludipDash"),
    path('ludip/',views.ludipView,name="ludipView"),
    path('ludipSaveParams/',views.ludipSaveParams,name="ludipSaveParams"),
    path('ludipJsonList/',views.ludipJsonList,name="ludipJsonList"),
    path('lupidUpdateParams/<int:id>',views.lupidUpdateParams,name="lupidUpdateParams"),
    path('lupidDeleteParams/<int:id>',views.lupidDeleteParams,name="lupidDeleteParams"),
    ]
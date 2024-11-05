from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('dash-admin/campus/',views.campusView,name="campus"),
    path('campusJsonList/',views.campusJsonList, name="campusJsonList"),
    path('save-campus/',views.saveUpdateCampusParams,name="saveUpdateCampusParams" ),
    path('delete-campus/<int:id>',views.deleteCampusParams,name="deleteCampusParams" ),

    path('dash-admin/division/',views.divisionView,name="division"),
    path('divisionJsonList/',views.divisionJsonList, name="divisionJsonList"),
    path('save-division/',views.saveUpdateDivParams,name="saveUpdateDivParams" ),
    path('delete-division/<int:id>',views.deleteDivParams,name="deleteDivParams" ),

    path('dash-admin/component/',views.componentView,name="componentView"),
    path('componentJsonList/',views.componentJsonList, name="componentJsonList"),
    path('getCompJsonList/',views.getCompJsonList, name="getCompJsonList"),
    path('save-component/',views.saveUpdateCompParams,name="saveUpdateCompParams" ),
    path('delete-component/<int:id>',views.deleteCompParams,name="deleteCompParams" ),
    
    path('dash-admin/gad/',views.gadView,name="gadView"),
    path('gadJsonList/',views.gadJsonList, name="gadJsonList"),
    path('save-gad-details/',views.saveUpdateGadDetails,name="saveUpdateGadDetails"),
    path('delete-gad/<int:id>',views.deleteGadParams,name="deleteGadParams" ),
 
    path('dash-admin/dashboard-gad/',views.gadDashView,name="gadDashView"),
    path('dash-admin/dashboard-gad-all/',views.gadDashAllView,name="gadDashAllView"),
    path('dash-admin/dashboard-gad-new/',views.gadDashNewView,name="gadDashNewView"),
   
]
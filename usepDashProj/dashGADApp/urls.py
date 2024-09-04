from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('campus/',views.campusView,name="campus"),
    path('campusJsonList/',views.campusJsonList, name="campusJsonList"),
    path('save-campus/',views.saveUpdateCampusParams,name="saveUpdateCampusParams" ),
    path('delete-campus/<int:id>',views.deleteCampusParams,name="deleteCampusParams" ),

    path('division/',views.divisionView,name="division"),
    path('divisionJsonList/',views.divisionJsonList, name="divisionJsonList"),
    path('save-division/',views.saveUpdateDivParams,name="saveUpdateDivParams" ),
    path('delete-division/<int:id>',views.deleteDivParams,name="deleteDivParams" ),

    path('component/',views.componentView,name="componentView"),
    path('componentJsonList/',views.componentJsonList, name="componentJsonList"),
    path('getCompJsonList/',views.getCompJsonList, name="getCompJsonList"),
    path('save-component/',views.saveUpdateCompParams,name="saveUpdateCompParams" ),
    path('delete-component/<int:id>',views.deleteCompParams,name="deleteCompParams" ),
    
    path('gad/',views.gadView,name="gadView"),
    path('gadJsonList/',views.gadJsonList, name="gadJsonList"),
    path('save-gad-details/',views.saveUpdateGadDetails,name="saveUpdateGadDetails"),
    path('delete-gad/<int:id>',views.deleteGadParams,name="deleteGadParams" ),
 
    path('dashboard-gad/',views.gadDashView,name="gadDashView"),
    path('dashboard-gad-all/',views.gadDashAllView,name="gadDashAllView"),
    path('dashboard-gad-new/',views.gadDashNewView,name="gadDashNewView"),
   
]
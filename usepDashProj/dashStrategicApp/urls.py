from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('dash-admin',views.dashboard,name="dashboard"),
    path('dash-admin/dashboard-strategic/',views.stratDash,name="stratDash"),
    path('dashAnnTargetJsonList/',views.dashAnnTargetJsonList,name="dashAnnTargetJsonList"),
  
    path('dash-admin/demo-dash-strat/',views.demoDash,name="demoDash"),
    path('saveDashRecord/',views.saveDashRecord, name="saveDashRecord"),
   
    path('dash-admin/dashboard-scorecard/',views.scoreDash,name="scoreDash"),
    path('dashScorecardJsonList/<str:year>/',views.dashScorecardJsonList,name="dashScorecardJsonList"),
    path('saveScorecard/',views.saveScorecardParams, name="saveScorecardParams"),
   
    path('area/',views.stratAreaView,name="stratAreaView"),
    path('areaJsonList/',views.areaJsonList,name="analJsonList"),
    path('save-area/',views.areaSaveParams,name="areaSaveParams"),
    path('update-area/<int:id>',views.areaUpdateParams,name="areaUpdateParams"),
    path('delete-area/<int:id>',views.areaDeleteParams,name="areaDeleteParams"),
    
    path('objective/',views.stratObjView,name="stratObjView"),
    path('objJsonList/',views.objJsonList,name="objJsonList"),
    path('save-objective/',views.objSaveParams,name="objSaveParams"),
    path('update-objective/<int:id>',views.objUpdateParams,name="objUpdateParams"),
    path('delete-objective/<int:id>',views.ObjDeleteParams,name="ObjDeleteParams"),

    path('indicator/',views.stratIndView,name="stratIndView"),
    path('indJsonList/',views.indJsonList,name="indJsonList"),
    path('save-indicator/',views.indSaveParams,name="indSaveParams"),
    path('update-indicator/<int:id>',views.indUpdateParams,name="indUpdateParams"),
    path('delete-indicator/<int:id>',views.indDeleteParams,name="indDeleteParams"),
    
    path('reference/',views.referenceView,name="referenceView"),
    path('refJsonList/',views.refJsonList,name="refJsonList"),
    path('refSaveUpdateParams/',views.refSaveUpdateParams,name="refSaveUpdateParams"),
    path('refDeleteParams/<int:id>',views.refDeleteParams,name="refDeleteParams"),

    path('strat-template-list/',views.stratTemplateListView,name="stratTemplateListView"),
    path('strat-template/',views.stratTemplateView,name="stratTemplateView"),
    path('stratRawJsonList/',views.stratRawJsonList,name="stratRawJsonList"),
    path('tempJsonList/',views.tempJsonList,name="tempJsonList"),

    path('stratTempJsonList/<int:id>',views.stratTempJsonList, name="stratTempJsonList"),
    path('saveTemplateParams/',views.saveTemplateParams,name="saveTemplateParams"),

    path('strat-template-1/',views.stratTemplateView1,name="stratTemplateView1"),
    ]
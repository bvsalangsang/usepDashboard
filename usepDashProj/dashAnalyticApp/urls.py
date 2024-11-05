from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('dash-admin/dashboard-analytic/',views.anaDashboardView,name="anaDashboardView"),
    path('dash-admin/analytics/',views.analyticsView,name="analyticsView"),
    path('analJsonList/',views.analJsonList,name="analJsonList"),
    path('analSaveParams/',views.analSaveParams,name="analSaveParams"),
    path('analUpdateParams/<int:id>',views.analUpdateParams,name="analUpdateParams"),
    path('analDeleteParams/<int:id>',views.analDeleteParams,name="analDeleteParams"),
    path('getAnalytic/<int:id>',views.getAnalytic,name="getAnalytic"),
 

    path('dash-admin/board-passers/',views.boardPassersView,name="boardPassersView"),
    path('boardPasserJsonList/',views.boardPasserJsonList,name="boardPasserJsonList"),
    path('save-board-passer/',views.boardPasserSaveParams,name="boardPasserSaveParams"),
    path('update-board-passer/<int:id>',views.boardPasserUpdateParams,name="boardPasserSaveParams"),
    path('delete-board-passer/<int:id>',views.boardPasserDeleteParams,name="boardPasserDeleteParams"),

    path('dash-admin/employability/',views.employabilityView,name="employabilityView"),
    path('employabilityJsonList/',views.employabilityJsonList,name="employabilityJsonList"),
    path('save-employability/',views.employabilitySaveParams,name="employabilitySaveParams"),
    path('update-employability/<int:id>',views.employabilityUpdateParams,name="employabilityUpdateParams"),
    path('delete-employability/<int:id>',views.employabilityDeleteParams,name="employabilityDeleteParams"),
   
    path('dash-admin/ched-rdc-identified/',views.chedRdcView,name="chedRdcView"),
    path('chedRdcJsonList/',views.chedRdcJsonList,name="chedRdcJsonList"),
    path('save-ched-rdc-identified/',views.chedRdcSaveParams,name="chedRdcSaveParams"),
    path('update-ched-rdc-identified/<int:id>',views.chedRdcUpdateParams,name="chedRdcUpdateParams"),
    path('delete-ched-rdc-identified/<int:id>',views.chedRdcDeleteParams,name="chedRdcDeleteParams"),
 
    path('dash-admin/accreditation/',views.accredView,name="accredView"),
    path('accredJsonList/',views.accredJsonList,name="accredJsonList"),
    path('save-accreditation/',views.accredSaveParams,name="accredSaveParams"),
    path('update-accreditation/<int:id>',views.accredUpdateParams,name="accredUpdateParams"),
    path('delete-accreditation/<int:id>',views.accredDeleteParams,name="accredDeleteParams"),
   
    path('dash-admin/faculty-research/',views.gradResView,name="gradResView"),
    path('gradResJsonList/',views.gradResJsonList,name="gradResJsonList"),
    path('save-faculty-research/',views.gradResSaveParams,name="gradResSaveParams"),
    path('update-faculty-research/<int:id>',views.gradResUpdateParams,name="gradResUpdateParams"),
    path('delete-faculty-research/<int:id>',views.gradResDeleteParams,name="gradResDeleteParams"),
   
    path('dash-admin/research-degree/',views.resDegView,name="resDegView"),
    path('resDegJsonList/',views.resDegJsonList,name="resDegJsonList"),
    path('save-research-degree/',views.resDegSaveParams,name="resDegSaveParams"),
    path('update-research-degree/<int:id>',views.resDegUpdateParams,name="resDegUpdateParams"),
    path('delete-research-degree/<int:id>',views.resDegDeleteParams,name="resDegDeleteParams"),

    path('dash-admin/accredited-grad-programs/',views.accrGradProgView,name="accrGradProgView"),
    path('accrGradProgJsonList/',views.accrGradProgJsonList,name="accrGradProgJsonList"),
    path('save-accr-grad-prog/',views.accrGradProgSaveParams,name="accrGradProgSaveParams"),
    path('update-accr-grad-prog/<int:id>',views.accrGradProgUpdateParams,name="accrGradProgUpdateParams"),
    path('delete-accr-grad-prog/<int:id>',views.accrGradProgDeleteParams,name="accrGradProgDeleteParams"),
  
    path('dash-admin/research-output/',views.resOutputView,name="resOutputView"),
    path('resOutputJsonList/',views.resOutputJsonList,name="resOutputJsonList"),
    path('save-research-output/',views.resOutputSaveParams,name="resOutputSaveParams"),
    path('update-research-output/<int:id>',views.resOutputUpdateParams,name="resOutputUpdateParams"),
    path('delete-research-output/<int:id>',views.resOutputDeleteParams,name="resOutputDeleteParams"),

    path('dash-admin/research-complete/',views.resCompleteView,name="resCompleteView"),
    path('resCompleteJsonList/',views.resCompleteJsonList,name="resCompleteJsonList"),
    path('save-research-complete/',views.resCompleteSaveParams,name="resCompleteSaveParams"),
    path('update-research-complete/<int:id>',views.resCompleteUpdateParams,name="resCompleteUpdateParams"),
    path('delete-research-complete/<int:id>',views.resCompleteDeleteParams,name="resCompleteDeleteParams"),
   
    path('dash-admin/research-published/',views.resPublishedView,name="resPublishedView"),
    path('resPublishedJsonList/',views.resPublishedJsonList,name="resPublishedJsonList"),
    path('save-research-published/',views.resPublishedSaveParams,name="resPublishedSaveParams"),
    path('update-research-published/<int:id>',views.resPublishedUpdateParams,name="resPublishedUpdateParams"),
    path('delete-research-published/<int:id>',views.resPublishedDeleteParams,name="resPublishedDeleteParams"),
    
    path('dash-admin/active-partner/',views.actPartnerView,name="actPartnerView"),
    path('actPartnerJsonList/',views.actPartnerJsonList,name="actPartnerJsonList"),
    path('save-active-partner/',views.actPartnerSaveParams,name="actPartnerSaveParams"),
    path('update-active-partner/<int:id>',views.actPartnerUpdateParams,name="actPartnerUpdateParams"),
    path('delete-active-partner/<int:id>',views.actPartnerDeleteParams,name="actPartnerDeleteParams"),
  
    path('dash-admin/trainees/',views.traineesView,name="traineesView"),
    path('traineesJsonList/',views.traineesJsonList,name="traineesJsonList"),
    path('save-trainees/',views.traineesSaveParams,name="traineesSaveParams"),
    path('update-trainees/<int:id>',views.traineesUpdateParams,name="traineesUpdateParams"),
    path('delete-trainees/<int:id>',views.traineesDeleteParams,name="traineesDeleteParams"),
   
    path('dash-admin/extension-program/',views.extProgramView,name="extProgramView"),
    path('extProgramJsonList/',views.extProgramJsonList,name="extProgramJsonList"),
    path('save-extension-program/',views.extProgramSaveParams,name="extProgramSaveParams"),
    path('update-extension-program/<int:id>',views.extProgramUpdateParams,name="extProgramUpdateParams"),
    path('delete-extension-program/<int:id>',views.extProgramDeleteParams,name="extProgramDeleteParams"),
    
    path('dash-admin/beneficiary/',views.beneficiaryView,name="beneficiaryView"),
    path('beneficiaryJsonList/',views.beneficiaryJsonList,name="beneficiaryJsonList"),
    path('save-beneficiary/',views.beneficiarySaveParams,name="beneficiarySaveParams"),
    path('update-beneficiary/<int:id>',views.beneficiaryUpdateParams,name="beneficiaryUpdateParams"),
    path('delete-beneficiary/<int:id>',views.beneficiaryDeleteParams,name="beneficiaryDeleteParams"),
  
]



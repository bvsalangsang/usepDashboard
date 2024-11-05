"""
URL configuration for usepDashProj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from dashLudipApp import urls
from dashStrategicApp import urls
from dashAnalyticApp import urls
from dashGADApp import urls
from dashSiteApp import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashLudipApp.urls')),
    path('', include('dashStrategicApp.urls')), 
    path('', include('dashAnalyticApp.urls')), 
    path('', include('dashGADApp.urls')), 
    path('', include('dashSiteApp.urls')), 
]

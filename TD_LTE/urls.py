"""TD_LTE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from Log import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
   # url(r'^utest/', views.upload_tbCell),
    url(r'^uploadTbCell/', views.upload_tbCell, name="upTbCellIndex"),
    #url(r'^stest/', show_data),
    url(r'^login/', views.login, name="loginIndex"),
    url(r'^user/', views.user, name="userIndex"),
    url(r'^bar/', views.progress_bar, name="barIndex"),
    url(r'^download/', views.download_table, name="downloadIndex"),
    url(r'^preview/', views.download_preview, name="previewIndex"),
    url(r'^searchCell/', views.search_sql_cell, name="searchCellIndex"),
    url(r'^searchEnodeb/', views.search_sql_eNodeb, name="searchEnodebIndex"),
    url(r'^searchKPI/', views.search_sql_KPI, name="searchKPIIndex"),
    url(r'^searchPRB/', views.search_sql_PRB, name="searchPRBIndex"),
    url(r'^analy3cell/', views.analyse_python_3cell, name="analy3cellIndex"),
    url(r'^analyC2I/', views.analyse_C2I, name="analyC2IIndex"),
    #######################
#    url(r'^test/', views.import_table_from_excel)
]

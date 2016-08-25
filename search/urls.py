from django.conf.urls import url

from worksheet.search import views

urlpatterns = [
    url(r'^search$', views.search, name='search'),
    url(r'^modify$', views.modify, name='modify'),
    url(r'^search_result',views.search_result,name='search_result')
]
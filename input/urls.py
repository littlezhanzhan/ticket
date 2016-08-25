from django.conf.urls import url

from worksheet.input import views

urlpatterns = [
    url(r'^input', views.input, name='input'),
    url(r'^$', views.input, name='input'),
]
from django.conf.urls import url

from worksheet.count import views

urlpatterns = [
    url(r'^count$', views.count, name='count'),
    url(r'^count_result', views.count_result, name='count_result'),
]
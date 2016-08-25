# coding=utf-8
import django.utils.timezone as timezone
from django.shortcuts import render
from worksheet.models.models import User, WorkSheet
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.messages.api import success
from django.contrib.messages.apps import MessagesConfig

# Create your views here.


def input(request):
    now = timezone.localtime(timezone.now())
  
    count_num = WorkSheet.objects.count()
#     sheet_type = request.POST.get('type', None)
    #if sheet_type is not None:
     
     
    num = now.strftime('%Y%m%d%H%M%S') + str(count_num + 1)
    account = request.GET.get('account', False)
    if account:                                          #判断account是否为空   
        try: 
            User.objects.create(telnumber = account)     #用户直接插入用户表
        except IntegrityError:                           #非新用户，忽略错误
            messages.add_message(request,messages.SUCCESS,'您不是第一次输入')
            pass  
        userid = User.objects.get(telnumber = account)
        userid.worksheet_set.create(                      #数据存入数据库
            sheet_number = num,
            client_type = request.GET.get('client'),
            sheet_type = request.GET.get('type'),
            time = request.GET.get('date'),
            content = request.GET.get('content'),
            method = request.GET.get('method'))           
    messages.add_message(request,messages.SUCCESS,'存储成功')  
    return render(request, 'worksheet/input.html')
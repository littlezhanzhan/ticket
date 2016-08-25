# coding=utf-8
from django.shortcuts import render,render_to_response
from worksheet.models.models import WorkSheet, User
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.


def search(request):
    return render(request, 'worksheet/search.html')


def modify(request):
    selected_worksheet = WorkSheet.objects.get(pk=request.POST.get('id'))

    selected_worksheet.content = request.POST.get('content')
    selected_worksheet.method = request.POST.get('method')
    selected_worksheet.client = request.POST.get('client')
    selected_worksheet.type = request.POST.get('type')
    selected_worksheet.date = request.POST.get('date')
    selected_worksheet.save()

    return HttpResponse("修改成功") 


def get_Kwargs(data={}):
    kwargs = {}
    for (k, v) in data.items():
        if v != u'0':
            if v != u'':
                if v is not None:
                    kwargs[k] = v
    return kwargs


def search_result(request):
    account = request.GET.get('account')
    data = {'client_type': request.GET.get('client'),
            'sheet_type': request.GET.get('type'),
            'time__gte': request.GET.get('startDate'),
            'time__lte': request.GET.get('endDate'),
            }
    print account, data
    if account != '':
        try:
            a = User.objects.get(telnumber=account)
        except Exception:
            return HttpResponseRedirect('/worksheet/search', '账号不存在！')
        sheet1 = a.worksheet_set.all()
        kwargs1 = get_Kwargs(data)
        print kwargs1, '1'
        if kwargs1 == {}:
            results = sheet1
        else:
            results = sheet1.filter(**kwargs1)
    else:
        sheet2 = WorkSheet.objects.all()
        kwargs2 = get_Kwargs(data)
        print kwargs2, '2'
        if kwargs2 == {}:
            results = sheet2
        else:
            results = sheet2.filter(**kwargs2)
            
    print results.count()
    result = results.order_by("-time")
    clients_list = ['安卓端','苹果端','平台侧','web','PC端']
    type_list = ['上传','下载','解绑','换绑','客户端异常','账号异常','VIP开通','客户端bug','文件损坏','网络故障','dns问题']
    return render_to_response('search.html', {'results': result,'clients_list':clients_list,'type_list':type_list})


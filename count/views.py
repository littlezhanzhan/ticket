from django.shortcuts import render_to_response, render

from worksheet.models.models import WorkSheet

# Create your views here.


def count(request):
    clients = []
    types = []
    return render(request, 'worksheet/count.html', {'client': clients, 'type': types})


def count_result(request):
    start_date = request.GET.get('startDate', False)
    end_date = request.GET.get('endDate', False)

    if start_date and end_date:
        clients_all = WorkSheet.objects.filter(time__gte=start_date, time__lte=end_date)
        c1 = clients_all.filter(client_type=1).count()
        c2 = clients_all.filter(client_type=2).count()
        c3 = clients_all.filter(client_type=3).count()
        c4 = clients_all.filter(client_type=4).count()
        c5 = clients_all.filter(client_type=5).count()
        clients = [c1, c2, c3, c4, c5]

        types_all = WorkSheet.objects.filter(time__gte=start_date, time__lte=end_date)
        t1 = types_all.filter(sheet_type=1).count()
        t2 = types_all.filter(sheet_type=2).count()
        t3 = types_all.filter(sheet_type=3).count()
        t4 = types_all.filter(sheet_type=4).count()
        t5 = types_all.filter(sheet_type=5).count()
        t6 = types_all.filter(sheet_type=6).count()
        t7 = types_all.filter(sheet_type=7).count()
        t8 = types_all.filter(sheet_type=8).count()
        t9 = types_all.filter(sheet_type=9).count()
        t10 = types_all.filter(sheet_type=10).count()
        t11 = types_all.filter(sheet_type=11).count()
        types = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11]

    else:
        clients_all = WorkSheet.objects.all()
        c1 = clients_all.filter(client_type=1).count()
        c2 = clients_all.filter(client_type=2).count()
        c3 = clients_all.filter(client_type=3).count()
        c4 = clients_all.filter(client_type=4).count()
        c5 = clients_all.filter(client_type=5).count()
        clients = [c1, c2, c3, c4, c5]

        types_all = WorkSheet.objects.all()
        t1 = types_all.filter(sheet_type=1).count()
        t2 = types_all.filter(sheet_type=2).count()
        t3 = types_all.filter(sheet_type=3).count()
        t4 = types_all.filter(sheet_type=4).count()
        t5 = types_all.filter(sheet_type=5).count()
        t6 = types_all.filter(sheet_type=6).count()
        t7 = types_all.filter(sheet_type=7).count()
        t8 = types_all.filter(sheet_type=8).count()
        t9 = types_all.filter(sheet_type=9).count()
        t10 = types_all.filter(sheet_type=10).count()
        t11 = types_all.filter(sheet_type=11).count()
        types = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11]

    return render_to_response('worksheet/count.html', {'client': clients, 'type': types})
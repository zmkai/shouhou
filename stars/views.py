import json

from django.db.models import Avg
from django.http import HttpResponse
from django.views.generic import View

from stars.models import Stars


class StarsView(View):
    def createstar(self,star,weibao_account):
        stars=Stars.objects.create(star=star,weibao_account=weibao_account)
        return stars
    # 统计所有维保人员的星级
    def get(self, request):
        avgs = Stars.objects.values('weibao_account').annotate(staravg=Avg('star'))
        avglist = []
        for i in avgs:
            avglist.append(i)
        return HttpResponse(status=200,
                            content=json.dumps({'code': 0, 'message': 'query successful', 'data': avglist}))
from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

# Create your views here.
from parking_passport_client.django.decorators import token_required
import json

from django.db.models import F
from django.http import HttpResponse, HttpResponseBadRequest

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from repair.forms import RepairForm
from repair.models import Repair


@method_decorator(csrf_exempt,name='dispatch')
class RepairView(View):
    #客户申请维修单
    @token_required()
    def post(self,request):
        rep=RepairForm(request.POST)
        print(type(rep))
        if not rep.is_valid():
            return HttpResponseBadRequest(status=422,content=json.dumps({'code':1,'message':'Submitted failure'}))
        repair = Repair.objects.create(customer_id=rep.data.get('customer_id'),depot_id=rep.data.get('depot_id'),
                                       title=rep.data.get('title'),problem_desciption=rep.data.get('problem_desciption'))
        return HttpResponse(status=201, content=json.dumps({'code':0,'message':'Submitted successfully'}))


    #客户查询维修单(分页查询)
    def get(self,request,customer_id):
        repairs = Repair.objects.filter(customer_id=customer_id).order_by('create_time')
        page = request.GET.get('page')
        pageSize = int(request.GET.get('pageSize'))
        response = {}
        repair_list = Repair.objects.all()
        paginator = Paginator(repair_list, pageSize)
        response['total'] = paginator.count
        try:
            repairs = paginator.page(page)
        except PageNotAnInteger:
            repairs = paginator.page(1)
        except EmptyPage:
            repairs = paginator.page(paginator.num_pages)
        response['list'] = json.loads(serializers.serialize('json', repairs))
        return HttpResponse(status=200,content=json.dumps({'code':0,'message':'query successfully','data':response['list']}))








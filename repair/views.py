import datetime
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import json
from django.http import HttpResponse, HttpResponseBadRequest
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from repair.forms import RepairForm, RepairForm1
from repair.models import Repair


class RepairView(View):
    #客户申请维修单
    #@method_decorator(login_required(login_url="#"))
    def post(self,request):
        rep = RepairForm(request.POST)
        print(type(rep))
        if not rep.is_valid():
            return HttpResponseBadRequest(status=422,content=json.dumps({'code':1,'message':'Submitted failure'}))
        repair = Repair.objects.create(customer_id=rep.data.get('customer_id'),depot_id=rep.data.get('depot_id'),
                                       title=rep.data.get('title'),problem_desciption=rep.data.get('problem_desciption'))
        return HttpResponse(status=201, content=json.dumps({'code':0,'message':'Submitted successfully'}))

    #客户查询维修单(分页查询)
    # @method_decorator(login_required(login_url="#"))
    def get(self,request,customer_id):
        rep = RepairForm1(request.GET)
        if not rep.is_valid():
            return HttpResponseBadRequest(status=422, content=json.dumps({'code': 1, 'message': 'Submitted failure'}))
        repairs = Repair.objects.filter(customer_id=customer_id).order_by('create_time')
        page = rep.data.get('page')
        pageSize = int(rep.data.get('pageSize'))
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

    # 通过JSON格式提交请求体，可以根据维保单ID修改问题标题及问题描述
    #@method_decorator(login_required(login_url="#"))
    def put(self,request,number_id):
        stream = request.body.decode()
        json_data = json.loads(stream)
        repair = Repair.objects.filter(number_id=number_id).update(title=json_data['title'],problem_desciption=json_data['problem_desciption'],update_time=datetime.datetime.now())
        return HttpResponse(status=200,content=json.dumps({'code':0,'message':'put successfully'}))














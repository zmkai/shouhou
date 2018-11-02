
from django.shortcuts import render
from stars.models import Stars
from django.contrib.auth.decorators import login_required
from repair.forms import ReceivedForm, ReceivingForm, UnReceiveForm
import datetime
import time
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import json
from django.http import HttpResponse, HttpResponseBadRequest
from django.utils.decorators import method_decorator
from django.views.generic import View

from repair.forms import RepairForm_p, RepairForm_g
from repair.models import Repair


class RepairView(View):
    # 客户申请维修单
    @method_decorator(login_required(login_url="#"))
    def post(self,request):
        rep = RepairForm_p(request.POST)
        print(type(rep))
        if not rep.is_valid():
            return HttpResponseBadRequest(status=422,content=json.dumps({'code':1,'message':'Submitted failure'}))
        repair = Repair.objects.create(customer_id=rep.data.get('customer_id'),depot_id=rep.data.get('depot_id'),
                                       title=rep.data.get('title'),problem_desciption=rep.data.get('problem_desciption'))
        return HttpResponse(status=201, content=json.dumps({'code':0,'message':'Submitted successfully'}))

    # 客户查询维修单(分页查询)
    @method_decorator(login_required(login_url="#"))
    def get(self,request,customer_id):
        print(customer_id)
        rep = RepairForm_g(request.GET)
        if not rep.is_valid():
            return HttpResponseBadRequest(status=422, content=json.dumps({'code': 1, 'message': 'Submitted failure'}))
        repairs = Repair.objects.filter(customer_id=customer_id).order_by('create_time')
        print(repairs)
        page = rep.data.get('page')
        pageSize = int(rep.data.get('pageSize'))
        response = {}
        paginator = Paginator(repairs, pageSize)
        response['total'] = paginator.count
        try:
            repair = paginator.page(page)
        except PageNotAnInteger:
            repair = paginator.page(1)
        except EmptyPage:
            repair = paginator.page(paginator.num_pages)
        response['list'] = json.loads(serializers.serialize('json', repair))
        return HttpResponse(status=200,content=json.dumps({'code':0,'message':'query successfully','data':response['list']}))

    # 通过JSON格式提交请求体，可以根据维保单ID修改问题标题及问题描述
    @method_decorator(login_required(login_url="#"))
    def put(self,request,number_id):
        stream = request.body.decode()
        json_data = json.loads(stream)
        repair = Repair.objects.filter(number_id=number_id).update(title=json_data['title'],problem_desciption=json_data['problem_desciption'],update_time=datetime.datetime.now())
        return HttpResponse(status=200,content=json.dumps({'code':0,'message':'put successfully'}))


class UnReceiveView(View):
    @method_decorator(login_required(login_url='#'))
    # 查看可接单，显示信息为维保单的标题
    def get(self, request):
        res = UnReceiveForm(request.GET)
        if not res.is_valid():
            return HttpResponse(422)
        datas = Stars.objects.filter(weibao_account=res.data.get('weibao_account'))
        num = datas.count()
        stars = 0
        for data in datas:
            stars += data.star
        stars = stars / num
        print(stars)
        list = []
        if stars <= 2:
            repair_forms = Repair.objects.filter(status=0).filter(
                create_time__lte=datetime.datetime.now() + datetime.timedelta(minutes=-5))
        elif stars < 4:
            repair_forms = Repair.objects.filter(status=0).filter(
                create_time__lte=datetime.datetime.now() + datetime.timedelta(minutes=-3))
        else:
            repair_forms = Repair.objects.filter(status=0)
        for repair_form in repair_forms:
            repair_form = repair_form.detail_info()
            title = repair_form['title']
            list.append(title)
        print(list)
        data_json = json.dumps(list)
        return HttpResponse(201, data_json)


class ReceivingView(View):
    # 获取当前时间
    def now_time(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

    @method_decorator(login_required(login_url='#'))
    # 查看显示表单标题的详细信息
    def get(self, request):
        res = ReceivingForm(request.GET)
        if not res.is_valid():
            return HttpResponse(422)
        # 返回维修表单的详细信息
        for repair_forms in Repair.objects.filter(number_id=res.data.get('number_id')):
            data = repair_forms.detail_info()
            print(data)
            print(type(data))
            data_json = json.dumps(data)
        return HttpResponse(201, data_json)


    # 抢单
    @method_decorator(login_required(login_url='#'))
    def put(self, request):
        stream = request.body.decode()
        json_data = json.loads(stream)
        repair_forms = Repair.objects.filter(number_id=json_data['number_id'])
        result = []
        for repair_form in repair_forms:
            result.append(repair_form.detail_info())
        if result[0]['status'] == '1':
            return HttpResponse(400)
        else:
            # 修改状态码，添加维保人员账号
            repair_forms.update(status='1', weibao_account=json_data['weibao_account'], receive_time=self.now_time())
            return HttpResponse(204)


class ReceivedView(View):
    def now_time(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

    @method_decorator(login_required(login_url='#'))
    # 查看已接单，显示信息为表单标题
    def get(self, request):
        res = ReceivedForm(request.GET)
        if not res.is_valid():
            return HttpResponse(422)
        list1 = []
        repairs = Repair.objects.filter(weibao_account=res.data.get('weibao_account'))
        if repairs.exists():
            for repair in repairs:
                repair = repair.detail_info()
                title = repair['title']
                # print(title)
                list1.append(title)
            print(list1)
            data_json = json.dumps(list1)
            # print(data_json)
            return HttpResponse(201,data_json)
        else:
            return HttpResponse(400)

    @method_decorator(login_required(login_url='#'))
    # 完成维修单
    def put(self, request):
        stream = request.body.decode()
        json_data = json.loads(stream)
        # 填写原因、解决办法、修改状态码
        Repair.objects.filter(number_id=json_data['number_id']).update(reason=json_data['reason'],
                                                                       solve_way=json_data['solve_way'],
                                                                       finish_status=1,
                                                                       update_time=self.now_time())

        return HttpResponse(204)








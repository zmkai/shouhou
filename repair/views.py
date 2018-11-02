from django.shortcuts import render
from django.views.generic import View
from repair.models import Repair
import json
from django.http import HttpResponse
import time
from stars.models import Stars
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from repair.form import ReceivedForm, ReceivingForm, UnReceiveForm
# from parking_passport_client.django.decorators import token_required
# Create your views here.


class UnReceiveView(View):
    @method_decorator(login_required(login_url='#'))
    # 查看可接单，显示信息为维保单的标题
    def get(self, request):
        # res = UnReceiveForm(request.GET)
        # if not res.is_valid():
        #     return HttpResponse(422)
        # data = Stars.objects.get(weibao_account=res.date.get('weibao_account'))
        # stars = data.star
        # print(stars)
        # if stars <= 2:
        #     pass
        # elif stars < 3:
        #     pass
        # else:
        #     pass
        list = []
        repair_forms = Repair.objects.filter(status=0)
        for repair_form in repair_forms:
            repair_form = repair_form.detail_info()
            title = repair_form['title']
            print(title)
            list.append(title)
            print(list)
        data_json = json.dumps(list)
        return HttpResponse(200, data_json)


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
        return HttpResponse(200, data_json)

    # 抢单
    @method_decorator(login_required)
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
            return HttpResponse(200)


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
            return HttpResponse(200,data_json)
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
        return HttpResponse(200)





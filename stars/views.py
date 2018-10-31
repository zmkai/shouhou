from django.shortcuts import render

# Create your views here.
from parking_passport_client.django.decorators import token_required
import json

from django.db.models import F
from django.http import HttpResponse

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from comment.forms import CommentForm
from comment.models import Comment
from repair.models import Repair
from stars.forms import StarsForm
from stars.models import Stars


@method_decorator(csrf_exempt, name='dispatch')
class StarsView(View):
    # 客户填写星级评价表
    def post(self, request):
        rep = StarsForm(request.POST)
        if not rep.is_valid():
            return HttpResponse(status=422, content=json.dumps({'code':1,'message':'Submitted failure'}))
        weibao_account=Repair.objects.get(number_id=rep.data.get('number_id')).weibao_account
        stars = Stars.objects.create(weibao_account=weibao_account,star=rep.data.get('star'))
        return HttpResponse(status=201, content=json.dumps({'code':0,'message':'Submitted successfully'}))







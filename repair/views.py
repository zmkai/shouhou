from django.shortcuts import render
from django.views.generic import View

from repair.models import Repair
import json
from django.http import HttpResponse
# from parking_passport_client.django.decorators import token_required
# Create your views here.


class Search(View):

    def get(self, request):
        repair_forms = Repair.objects.filter(status='0')
        print(repair_forms)
        return HttpResponse(200)


class Robbing(View):
    def put(self, request, number_id):
        Repair.objects.get(number_id=number_id).update(status='1')
        return HttpResponse(200)






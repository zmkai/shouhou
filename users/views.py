import json
import re

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import View

from .utils import JsonUtil
from .models import User


class UserView(View):
    '''
        添加一条维保人员信息
    '''
    @method_decorator(login_required)
    def post(self,request):
        print('post')
        params = JsonUtil.dict_request(request)
        print(type(params))
        try :
            user_name = params.get('username')
            telephone = params.get('telephone')
            password = telephone[-6:]
            print(password)
            user = User.objects.create_user(user_name," ",password)
            user.telephone = telephone
            user.name = params.get('name')
            #该属性为删除标记 ，为1则表示未删除，为0表示删除
            user.is_staff = True
            user.is_superuser = False
            user.save()
            json_str = JsonUtil.json_response('0','添加成功',None)
        except :
            print('异常')
            json_str = JsonUtil.json_response('1', '添加发生异常', None)
        return HttpResponse(json_str)

    '''
        根据传入的用户账号进行相关信息的修改或者修改用户密码
    '''
    @method_decorator(login_required(login_url='#'))
    def put(self,request):
        print('put')
        params = JsonUtil.dict_request(request)
        op_type = params.get('op_type')
        # 修改用户相关信息
        if op_type == 0:
            try:
                print(params)
                user_name = params.get('username')
                user = User.objects.get(username=user_name)
                # print(user.name)
                telephone = params.get('telephone')
                name = params.get('name')
                user.name = name
                user.telephone = telephone
                user.save()
                json_str = JsonUtil.json_response("0","修改成功",None)
            except:
                json_str = JsonUtil.json_response("1", "修改出现异常，请稍后再试", None)
            return  HttpResponse(json_str)
        else:
            # 修改密码
            try:
                user_name = params.get('username')
                user = User.objects.get(username=user_name)
                passwd = params.get('password')
                user.set_password(passwd)
                user.save()
                json_str = JsonUtil.json_response("0", "修改密码成功", None)
            except:
                json_str = JsonUtil.json_response("1", "修改密码出现异常，请稍后再试", None)
            return HttpResponse(json_str)
    '''
        根据用户账户进行删除
    '''
    @method_decorator(login_required(login_url='#'))
    def delete(self,request):
        print('put')
        try:
            params = JsonUtil.dict_request(request)
            print(params)
            user_name = params.get('username')
            user = User.objects.get(username=user_name)
            # print(user.name)
            user.is_staff = False
            user.save()
            json_str = JsonUtil.json_response("0", "删除成功", None)
        except:
            json_str = JsonUtil.json_response("1", "删除出现异常，请稍后再试", None)
        return HttpResponse(json_str)
    '''
        通过用户账号获取一个用户信息
    '''
    @method_decorator(login_required(login_url='#'))
    def get(self,request):
        print('put')
        try:
            params = request.GET
            # print(params)
            user_name = params.get('username')
            user = User.objects.filter(is_staff=True).filter(username__exact=user_name)[0]
            if user == None:
                json_str = JsonUtil.json_response("1", "当前未注册", None)
            else:
                print(user)
                # user = User.objects.get(username=user_name)
                user_dict = {'username':user.username,'telephone':user.telephone,'id':user.id}
                json_str = JsonUtil.json_response("0", "查询成功", json.dumps(user_dict))
        except:
            json_str = JsonUtil.json_response("1", "查询出现异常，请稍后再试", None)
        print(json_str)
        return HttpResponse(json_str)

class LoginView(View):
    '''
        登录
    '''
    def post(self,request):
        # 认证用户
        print('post')
        params = JsonUtil.dict_request(request)
        user_name = params.get('username')
        password = params.get('password')
        user = authenticate(username = user_name, password = password)
        if user is not None:
            # 登录
            login(request,user)
            json_str = JsonUtil.json_response("0", "登录成功",None)
        else:
            json_str = JsonUtil.json_response("1", "用户名不存在或者密码错误",None)
        return HttpResponse(json_str)

class UsersView(View):
    '''
        查询所有维保人员信息
    '''

    @method_decorator(login_required(login_url='#'))
    def get(self,request):
        print('get')
        try:
             users = User.objects.filter(is_staff=True).filter(is_superuser=False).values()
        except Exception:
            # print(Exception)
            print('异常')
            json_str = JsonUtil.json_response("1", "查询出现异常", None)
        else:
            users_list = []
            print(type(users))
            for user in users:
                user_dict = {'id':user.get('id'),'username':user.get('username'),'name':user.get('name'),'telephone':user.get('telephone')}
                users_list.append(user_dict)
            print(users_list)
            if len(users) > 0:
                json_str = JsonUtil.json_response("0","查询成功",json.dumps(users_list))
            else:
                json_str = JsonUtil.json_response("0","当前无数据",None)
        print(json_str)
        return HttpResponse(json_str)
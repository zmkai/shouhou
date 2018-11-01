import json
import re
from django.core import serializers
from django.db.models import QuerySet


class JsonUtil():
    '''
        将结果进行json封装
    '''
    @classmethod
    def json_response(cls, code, msg, data):
        json_str = {};
        dict_result = {"code":code,"msg":msg,"data":data}
        # print(dict_result)
        json_str.update(dict_result)
        json_str = json.dumps(json_str)
        return json_str

    '''
        
    '''
    @classmethod
    def dict_request(cls,request):
        params = request.body.decode()
        # 将json字符串中的单引号替换为双引号
        params = re.sub("\'", '\"', params)
        # 反序列化，转换为一个字典
        params = json.loads(params)
        return params

    @classmethod
    def querySet_list(cls,queryset):
        result_list = []
        for query in queryset:
            print(query.value_annotation)
        print(queryset.list())


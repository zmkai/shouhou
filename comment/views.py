import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import View
from comment.forms import CommentForm
from comment.models import Comment
from repair.models import Repair
from stars.models import Stars
from stars.views import StarsView


class CommentView(View):
    # 客户填写评价表(文字,星级)
    @method_decorator(login_required(login_url="#"))
    def post(self, request):
        rep = CommentForm(request.POST)
        if not rep.is_valid():
            return HttpResponse(status=422, content=json.dumps({'code': 1, 'message': 'Submitted failure'}))
        try:
            comment = Comment.objects.get(number_id=rep.data.get('number_id'))
        # 判断是否重复评论
        except Comment.DoesNotExist:
            weibao_account = Repair.objects.get(number_id=rep.data.get('number_id')).weibao_account
            comment = Comment.objects.create(number_id=rep.data.get('number_id'), weibao_account=weibao_account,
                                             comments=rep.data.get('comments'), remark=rep.data.get('remark'))
            #stars = Stars.objects.create(weibao_account=weibao_account, star=rep.data.get('star'))
            StarsView().createstar(rep.data.get('star'),weibao_account)
            return HttpResponse(status=201, content=json.dumps({'code': 0, 'message': 'Submitted successfully'}))
        else:
            return HttpResponse(status=405, content=json.dumps({'code': 1, 'message': 'comment finished'}))







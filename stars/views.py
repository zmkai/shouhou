from django.views.generic import View

from stars.models import Stars


class StarsView(View):
    def createstar(self,star,weibao_account):
        stars=Stars.objects.create(star=star,weibao_account=weibao_account)

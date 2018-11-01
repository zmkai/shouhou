from django.conf.urls import url
from repair.views import RepairsView, RepairView, ReceiveView


urlpatterns = [

    url(r'^repairs$', RepairsView.as_view()),
    url(r'^repair$', RepairView.as_view()),
    url(r'^receipts/(?P<weibao_account>.*)$', ReceiveView.as_view()),
    url(r'^repairing$', ReceiveView.as_view()),
    url(r'^repair/(?P<number_id>.*)$', RepairView.as_view())
]
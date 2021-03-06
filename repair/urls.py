from django.conf.urls import url
from repair.views import RepairView
from repair.views import ReceivedView, ReceivingView, UnReceiveView

urlpatterns=[
    url(r'^repairs$',RepairView.as_view()),
    url(r'^repairs/(?P<customer_id>\w+)$', RepairView.as_view()),
    url(r'^repair/(?P<number_id>\w+)$',RepairView.as_view()),
    url(r'^repaired$', ReceivedView.as_view()),
    url(r'^repairing$', ReceivingView.as_view()),
    url(r'^unrepairs$', UnReceiveView.as_view())
]


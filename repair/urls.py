from django.conf.urls import url
from repair.views import ReceivedView, ReceivingView, UnReceiveView


urlpatterns = [

    url(r'^repaired$', ReceivedView.as_view()),
    url(r'^repairing$', ReceivingView.as_view()),
    url(r'^unrepairs$', UnReceiveView.as_view())
]
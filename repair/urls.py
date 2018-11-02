from django.conf.urls import url
from repair.views import RepairView


urlpatterns=[
    url(r'^repairs$',RepairView.as_view()),
    url(r'^repairs/(?P<customer_id>\w+)$', RepairView.as_view()),
    url(r'^repair/(?P<number_id>\w+)$',RepairView.as_view()),
]
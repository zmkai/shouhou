from django.conf.urls import url

from stars.views import StarsView

urlpatterns=[
    url(r'^stars$',StarsView.as_view()),
]
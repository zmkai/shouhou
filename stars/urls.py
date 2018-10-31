from django.conf.urls import url

from comment.views import CommentView
from stars.views import StarsView

urlpatterns=[
    url(r'^stars',StarsView.as_view()),

]
from django.conf.urls import url

from comment.views import CommentView



urlpatterns=[
    url(r'^comments$',CommentView.as_view()),
]
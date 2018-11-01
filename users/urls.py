from django.conf.urls import url

from .views import UserView, UsersView, LoginView

urlpatterns = [
    url(r'^user$', UserView.as_view()),
    url(r'users$',UsersView.as_view()),
    url(r'^login$',LoginView.as_view()),
]
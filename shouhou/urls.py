"""shouhou URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
<<<<<<< HEAD
=======
from django.conf.urls import url,include
>>>>>>> 06c2e0cfb06ebaa3b6fb5c92513f86d0bb8e7b8a
from django.contrib import admin
from django.conf.urls import url,include

urlpatterns = [
<<<<<<< HEAD
    url(r'^', include('repair.urls'))
=======
    url(r'^admin/', admin.site.urls),
    url(r'^',include('users.urls'))
>>>>>>> 06c2e0cfb06ebaa3b6fb5c92513f86d0bb8e7b8a
]

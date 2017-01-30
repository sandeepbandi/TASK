"""TaskAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings


from TaskApp import views

router = routers.DefaultRouter() 

router.register(r'task', views.TaskViewSet)  


urlpatterns = [
    url(r'^register/$',views.CreateUserView.as_view(),name='user'),
    url(r'^',include(router.urls)),
    #url(r'^register/$',views.CreateUserView.as_view(),name='user'),
    url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



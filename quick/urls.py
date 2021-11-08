from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from myapi import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]

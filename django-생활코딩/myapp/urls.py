from django.urls import path, include
from .views import index, create, read

urlpatterns = [
    path('', index),
    path('create/', create),
    # 가변적인 값에 대해서는 <값의 이름>를 이용.
    path('read/<id>/', read),
]

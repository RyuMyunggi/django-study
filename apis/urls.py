from django.urls import path
from fastgram.apis.views import UserCreateView
from fastgram.apis.views import UserLoginView

urlpatterns = [
    path('v1/users/create/', UserCreateView.as_view(), name='apis_v1_user_create'),
    path('v1/users/login/', UserLoginView.as_view(), name='apis_v1_user_login'),
]
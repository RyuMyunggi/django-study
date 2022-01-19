from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

"""
django에서는 권한과 인증에 대한 구현이 되어있음
django에서 기본적으로 제공하는 User Model을 사용해도 좋지만 이후에 더 다양한 기능과 정보가 필요한 순간이 많음으로 그대로 사용하는 경우는 적음
settings.py에 'django.contrib.admin', 'django.contrib.auth', 'django.contrib.sessions'이 기본 구현되어 있음
"""


class User(AbstractUser):
    """
    커스텀 유저 모델
    기본 User의 동작은 그대로 하고 필드만 추가 정의
    """

    class GenderChoices(models.TextChoices):
        MALE = 'M', '남성'
        FEMALE = 'F', '여성'

    first_name = None
    last_name = None
    date_joined = None

    created_at = models.DateTimeField('등록날짜', auto_now_add=True)
    updated_at = models.DateTimeField('갱신날짜', auto_now_add=True)

    name = models.CharField('이름', max_length=30)
    gender = models.CharField('성별', max_length=1, blank=True, choices=GenderChoices.choices)
    profile_img = models.ImageField(
        '프로필이미지',
        blank=True,
        upload_to='account/profile_img/',
        help_text='gif/png/jpg 이미지를 업로드해주세요.'
    )


class UserReference1(models.Model):
    """
    get_user_model()
    현재 활성화 된 User model 인스턴스를 리턴
    django app이 로드 되는 순간에 실행되기 때문에 사용자 모델 객체를 리턴하지 않을 수도 있음(None)
    INSTALLED_APPS가 변경되는 등의 캐시에 있는 앱이 다시 로드 되는 경우에 위의 문제가 생길 확룔이 더 높음
    """
    class Meta:
        pass

    model = get_user_model()
    fields = ['username', 'email']


class UserReference2(models.Model):
    """
    외래키 모델을 전달 할 때 문자열로 전달
    외래키가 Import 될 때 모델 클래스 탐색에 실패하면 모든 앱이 로드 될 떄까지 탐색을 미룸
    항상 올바른 사용자 모델을 얻을 수 있
    """
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
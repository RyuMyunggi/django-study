from django.contrib import admin
from .models import User

"""
모델에 대한 관리용 인터페이스
컨텐츠를 편집할 수 있는 통합적인 인터페이스
"""


class UserAdmin(admin.ModelAdmin):
    """
    list_display: admin site에 보여질 필드를 정의하는 옵션
    search_fields: 사용자가 입력하는 검색어를 찾을 필드 지정 옵션
    list_filter: 사이트에 필터 활성화 옵션
    """
    list_display = ['username', 'email']
    search_fields = ['username']
    list_filter = ('gender',)


admin.site.register(User)


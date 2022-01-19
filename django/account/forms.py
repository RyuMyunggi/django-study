from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class LoginForm(AuthenticationForm):
    """
    AuthenticationForm: user가 존재하는지 검증하는 Model form
    사용자 인증
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = '아이디'
        self.fields['password'].label = '비밀번호'


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'name', 'gender', 'profile_img']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['name'].required = True
        self.fields['username'].lable = '아이디'
        self.fields['profile_img'].widget.attrs['accept'] = 'image/png', 'image/gif', 'image/jpeg'

    def clean_email(self):
        """
        cleaned_data(): 데이터의 유효성 검사뿐 아니라 일관된 형식으로 정규화
        is_valid()를 하지 않으면 Form 객체에 cleaned_data 속성이 없음
        Form 객체 안에서 정의한 필드 값에 대해서만 return
        """
        email = self.cleaned_data.get('email')
        if email:
            qs = User.objects.filter(email=email)
            if qs.exists():
                raise forms.ValidationError('이미 등록된 email입니다')
        return email
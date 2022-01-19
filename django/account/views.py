from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.views import logout_then_login, LoginView


from account.forms import RegisterForm, LoginForm


def logout_required(function=None, logout_url='/'):
    """
    유저 로그인을 하지 않은 사람에게만
    @decorator를 사용하여 어떠한 동작 전, 권한 여부 판단
    반대의 경우는 => from django.contrib.auth.decorators import login_required 장고 내장 인증 기능 이용
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated,
        login_url=logout_url,

    )
    if function:
        return actual_decorator(function)
    return actual_decorator


class MyLoginView(SuccessMessageMixin, LoginView):
    """
    django는 class based view를 작성하는 표준화된 방법을 제공
    """
    form_class = LoginForm
    template_name = 'template_root/html.html'
    next_page = '/'

    def valid_login(self, request):
        form = self.form_class
        username = form.username
        password = form.password
        user = authenticate(
            username=username,
            password=password
        )

        if user:
            auth_login(request, user)
            return redirect(self.next_page)
        else:
            messages.error(request, '일치하는 유저정보가 없습니다')


@logout_required()
def login(request: HttpRequest):
    return MyLoginView.as_view()(request)


def logout(request: HttpRequest):
    """
    ex) 로그인을 실패했을 때 사용자가 확인할 수 있게 알람의 띄워야함. js에서는 alert
    message framework를 사용하면 쉽게 띄울 수 있음
    1회성 메시지를 담는 용도로 사용. 메시지 등급이 있음. 자세한 건 messages level method 참고(warning, success, info ..)
    request를 통해 messages로 넘어옴
    """
    messages.success(request, '로그아웃 되었습니다')
    return logout_then_login(request)


@logout_required()
def register(request: HttpRequest):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            signed_user = form.save()
            auth_login(request, signed_user)
            messages.success(request, '회원가입을 환영합니다')
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
    else:
        form = RegisterForm()
    """
    render: api return 값으로 template 지정 가능
    redirect: 다른 url(api)로 이동. 호출만 가능
    """
    return render(request, 'html.html', {'data': 'data'})

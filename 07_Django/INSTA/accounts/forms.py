from django.contrib.auth.forms import UserCreationForm  # 회원가입
from django.contrib.auth.forms import UserChangeForm  # 회원정보 수정
from django.contrib.auth.forms import AuthenticationForm  # 로그인 관련 폼
from .models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class CustomUserAuthenticationForm(AuthenticationForm):

    class Meta(AuthenticationForm):
        model = User

from django import forms
from .models import Fcuser
from django.contrib.auth.hashers import check_password


class LoginForm(forms.Form):  # 두개의 필드를 사용하는 form이 하나 만들어 졌다.
    username = forms.CharField(
        error_messages={
            'required': '아이디를 입력해주세요'
        },
        max_length=32, label="사용자 이름")
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요'
        },
        widget=forms.PasswordInput, label="비밀번호")

    def clean(self):  # 검증!!!!
        # 얘는 이미 기본적으로 만들어 져있는 함수이기에 super를 통해서
        # 기존에 forms의 클래스 Form안의 clean 함수를 호출해주고
        cleaned_data = super().clean()
        # 만약 값이 들어있지 않았으면, 위의 코드에서 실패처리가 되어 나가게 된다.
        # 값이 다 들어왔다는 검증이 끝나면 아래의 코드를 실행한다.
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:  # 각 값들이 비어있지않고 들어있을때
            fcuser = Fcuser.objects.get(username=username)
            if not check_password(password, fcuser.password):  # 여기선 session을 적용하지 않을 것임
                # 특정 필드에 error을 넣는 함수
                self.add_error('password', '비밀번호가 틀렸습니다.')

            else:
                self.user_id = fcuser.id

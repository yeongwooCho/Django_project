from django import forms


class LoginForm(forms.Form):  # 두개의 필드를 사용하는 form이 하나 만들어 졌다.
    username = forms.CharField(max_length=32)
    password = forms.CharField()

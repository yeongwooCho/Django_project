from django import forms


class BoardForm(forms.Form):  # 두개의 필드를 사용하는 form이 하나 만들어 졌다.
    title = forms.CharField(
        error_messages={'required': '제목을 입력해주세요'}, max_length=128, label="제목")
    contents = forms.CharField(
        error_messages={'required': '내용을 입력해주세요'}, widget=forms.Textarea, label="내용")

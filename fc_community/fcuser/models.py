from django.db import models

# Create your models here.

# 장고에서 제공하는 models.Model클래스


class Fcuser(models.Model):
    objects = models.Manager()
    # username라는 필드를 만들고, 최대길이 64,
    # 여기서 verbose_name는 추후에 admin명령어를 사용할 때 거기서 필드(username)의 명명이다.
    # 다음과 같이 사용하면, 관리자 페이지에서 username가 영문이 아닌 사용자명 이라는 한글로 보이게 된다.
    username = models.CharField(
        max_length=64, verbose_name='사용자명')  # 문자열을 담을 수 있는 CharField

    useremail = models.EmailField(max_length=128, verbose_name="사용자이메일")

    # 비밀번호
    password = models.CharField(
        max_length=64, verbose_name='비밀번호')  # 문자열을 담을 수 있는 CharField

    # 가입한 날짜를 표시하자 (날짜와 시간을 표시할때 DateTimeField를 사용한다.), dttm은 datetime의 약자이다.
    registered_dttm = models.DateTimeField(
        auto_now=True, verbose_name='등록시간')  # 해당 클래스가 저장되는 시점에 자동으로 시간등록

    # 이 클래스를 만들었는데 데이터 베이스에 테이블 명을 지정하고 싶다!!!
    # 이런경우에 별도로 설정할 수 있다. 클래스안에 클래스를 만들어 내가 원하는 정보를 전달할 수 있다.
    # 기존의 등록된 app들과 구분하기 위해 table명을 다르게 설정할 때 주로 사용한다.

    # Fcuser object 는 위의 클래스를 문자열로 변환했을 때 나오는 값이다.
    # 파이썬에서는 클래스가 문자열로 변환했을 때 어떻게 변환을 할지 내장함수를 갖고 있다 -> __str__()

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'fast_campus_fcuser'
        verbose_name = "패스트컴퍼스 사용자"
        # 장고는 복수형을 리스트이름으로 보여준다. 이것도 지정할 수 잇다.
        verbose_name_plural = '패스트컴퍼스 사용자들'


# model 끝. 이제 데이터를 생성하고 삭제할 때, 별도로 설정할 필요없다. 이제 비지니스 모델을 만들면서 이 클래스를 만들어 생성과 삭제만 하면 된다
# 모델을 만들었으니 이제 모델을 관리 할 수 있는 관리자 페이지를 설정하고 활용하는 방법을 살펴보고, 그후 템플릿과 뷰를 만들자!

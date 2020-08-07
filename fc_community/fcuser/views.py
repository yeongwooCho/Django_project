from django.shortcuts import render, redirect
from .models import Fcuser
from django.http import HttpResponse  # 에러 메세지를 위함
from django.contrib.auth.hashers import make_password, check_password
from .form import LoginForm
# Create your views here.


def home(request):
    # 로그인이 되었는지 확인하기 위해, 세션의 정보를 가져와서 출력해보자!!
    user_id = request.session.get('user')
    if user_id:  # 유저가 있으면 사용자 정보를 가져오자
        # 세션의 유저키에 넣어던 것이 id 였다.
        fcuser = Fcuser.objects.get(pk=user_id)  # 해당 id인 모델을 가져온다.
        return HttpResponse(fcuser.username)

    return HttpResponse('Home')


def logout(request):
    if request.session['user']:
        del(request.session['user'])

    return redirect('/')


def login(request):  # 세션사용여부를 제외하면 계정만들기와 유사하다
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        # 데이터가 들어왔을 때 회원가입하는 코드를 작성해야한다.
        # html의 name필드의 데이터를 키로 해서 전달이 된다.
        # key에 대한 기본값이 없으면 None가 지정된다.
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}
        if not (username and useremail and password and re_password):
            res_data['error'] = '모든 값을 입력해야 합니다.'
        elif password != re_password:
            # return HttpResponse('비밀번호가 다릅니다.') # 페이지를 꽉채워 나온다...
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            # 이 데이터들로 fcuser을 생성할 것이다.
            fcuser = Fcuser(
                username=username,
                useremail=useremail,
                password=make_password(password)
            )
            fcuser.save()
        # 이것이 실제로 데이터베이스에 저장이 되는지 확인을 해보자

        # 그후 html코드를 반환하기에 다시 html파일이 나오는 것이다.
        return render(request, 'register.html', res_data)
        # 이렇게 되면 res_data가 html코드로 전달이 된다. 그럼 이것을 출력하는 코드를 html에 만들어 주자.

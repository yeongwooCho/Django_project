from django.shortcuts import render, redirect
from .models import Board
from .form import BoardForm
from fcuser.models import Fcuser
# Create your views here.


def board_detail(request, pk):  # 몇번째 글인지에 대한 정보가 필요하다
    # pk는 누군가에게 입력받아야하고, 주소로 입력받아야한다. /1 /2 이런것처럼
    # 그렇기에 이렇게 설정한 후 urls.py에 설정해주어야한다.

    board = Board.objects.get(pk=pk)
    return render(request, "board_detail.html", {'board': board})


def board_write(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            fcuser = Fcuser.objects.get(pk=user_id)

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = fcuser
            board.save()
            return redirect('/board/list')
    else:
        form = BoardForm()
    return render(request, 'board_write.html', {'form': form})


def board_list(request):
    # all은 다 가져오겠다는 뜻이고, 정렬또한 가능하다
    # (-는 역순 -> id역순으로 정렬) 즉, 최신것을 먼저 가져오겠다는 뜻이다.
    boards = Board.objects.all().order_by('-id')
    # 이제 templates에 전달해주면 된다.
    return render(request, 'board_list.html', {'boards': boards})

from django.shortcuts import render, redirect
from .models import Board
from .form import BoardForm
from fcuser.models import Fcuser
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from tag.models import Tag
# Create your views here.


def board_detail(request, pk):  # 몇번째 글인지에 대한 정보가 필요하다
    # pk는 누군가에게 입력받아야하고, 주소로 입력받아야한다. /1 /2 이런것처럼
    # 그렇기에 이렇게 설정한 후 urls.py에 설정해주어야한다.

    # 예외중에 클릭해서 들어온다면 괜찮지만, 임의의 주소를 통해서 들어오는 경우 문제가 된다.
    # But, 그 페이지가 존재하지 않는다면 문제가 된다.

    try:
        board = Board.objects.get(pk=pk)
    except ObjectDoesNotExist:  # 이때는 404페이지를 출력하도록 한다.
        raise Http404('게시글을 찾을 수 없습니다.')
    return render(request, "board_detail.html", {'board': board})


def board_write(request):
    # 사용자가 있는지 먼저 확인한다.
    if not request.session.get('user'):
        return redirect('/fcuser/login/')

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

            tags = form.cleaned_data['tags'].split(',')
            for tag in tags:
                if not tag:
                    continue

                _tag, _ = Tag.objects.get_or_create(
                    name=tag)  # 이름만 확인하면 되니깐
                board.tags.add(_tag)

            return redirect('/board/list')
    else:
        form = BoardForm()
    return render(request, 'board_write.html', {'form': form})


def board_list(request):
    # all은 다 가져오겠다는 뜻이고, 정렬또한 가능하다
    # (-는 역순 -> id역순으로 정렬) 즉, 최신것을 먼저 가져오겠다는 뜻이다.
    all_boards = Board.objects.all().order_by('-id')

    page = int(request.GET.get('p', 1))  # 페이지를 받자, 없으면 1페이지다
    paginator = Paginator(all_boards, 2)  # 전체 객체들을 넣어주고, 한페이지에 2개씩 나오도록 지정

    boards = paginator.get_page(page)  # page를 받아서 페이징기법을 사용한다.

    # 이제 templates에 전달해주면 된다.
    return render(request, 'board_list.html', {'boards': boards})

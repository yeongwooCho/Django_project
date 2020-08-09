from django.db import models


class Board(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=64, verbose_name='제목')
    contents = models.TextField(verbose_name="내용")
    # on_delete는 현재 게시글을 만들었는데 사용자가 삭제되었다면
    # ForeignKey가 가리키고있는 Fcuser모델을 어떻게 할지에 대한 정책이 존재해야함
    # CASCADE는 같이 삭제하겠다는 뜻이다.
    tags = models.ManyToManyField('tag.Tag', verbose_name='태그')
    writer = models.ForeignKey('fcuser.Fcuser', on_delete=models.CASCADE,
                               verbose_name='작성자')  # DB로 연결할수 있는방법
    registered_dttm = models.DateTimeField(auto_now=True, verbose_name='등록시간')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'fastcampus_board'
        verbose_name = "페스트컴퍼스 게시글"
        verbose_name_plural = '페스트컴퍼스 게시글'

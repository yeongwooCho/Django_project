from django.db import models

# Create your models here.


class Tag(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=32, verbose_name='태그명')
    registered_dttm = models.DateTimeField(auto_now=True, verbose_name='등록시간')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'fastcampus_tag'
        verbose_name = "페스트컴퍼스 태그"
        verbose_name_plural = '페스트컴퍼스 태그'

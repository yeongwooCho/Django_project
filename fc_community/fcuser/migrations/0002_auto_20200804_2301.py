# Generated by Django 3.0.8 on 2020-08-04 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fcuser',
            options={'verbose_name': '패스트컴퍼스 사용자', 'verbose_name_plural': '패스트컴퍼스 사용자들'},
        ),
    ]
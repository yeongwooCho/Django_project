from django.urls import path

from . import views

urlpatterns = [
    # register를 등록해보자
    # register함수를 등록한다.
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
    path('home/', views.home)
]

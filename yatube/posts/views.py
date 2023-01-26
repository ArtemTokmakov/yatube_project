from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Главная страница')


def group_post(request):
    return HttpResponse('Посты группы')


def group_posts(request, pk):
    return HttpResponse(f'Пост группы номер {pk}')


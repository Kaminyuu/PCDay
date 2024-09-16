from django.shortcuts import render


def index(request):
    context = {
        'title': 'PCday - Главная',
        'content': 'Магазин компьютерных комплектующих PCday',
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'PCday - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о том, почему данный сайт такой классный!'
    }
    return render(request, 'main/about.html', context)

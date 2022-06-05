from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def home_page(request):
    return HttpResponse("Рецепты")
    # можете добавить свои рецепты ;)

def recipe(request, name):
    context = {'recipe': DATA[f'{name}']}
    return render(request, 'calculator/index.html', servings(request, context))

def servings(request, context):
    servings = int(request.GET.get('servings', 1))
    recipe = {}
    for ingredient, amount in context['recipe'].items():
        amount *= servings
        recipe[f'{ingredient}'] = round(amount, 2)
    context = {'recipe': recipe}
    return context

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
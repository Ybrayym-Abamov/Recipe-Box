from django.shortcuts import render

from recipe.models import RecipeItem, Author

# Create your views here.


def index(request):
    data = RecipeItem.objects.all()
    return render(request, 'index.html', {'data': data})


def author(request, id):
    author = Author.objects.get(id=id)
    recipe = RecipeItem.objects.filter(author=author)
    return render(request, 'authorinfo.html', {'author': author, 'recipe': recipe})


def recipe(request, id):
    recipe = RecipeItem.objects.get(id=id)
    return render(request, 'recipe.html', {'recipe': recipe})

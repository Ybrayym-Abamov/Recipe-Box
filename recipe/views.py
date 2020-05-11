from django.shortcuts import render, reverse, HttpResponseRedirect

from recipe.models import RecipeItem, Author
from recipe.forms import RecipeAddForm, AuthorAddForm

# Create your views here.


def index(request):
    data = RecipeItem.objects.all()
    return render(request, 'index.html', {'data': data})


def recipeadd(request):
    html = "generic_form    .html"

    if request.method == "POST":
        form = RecipeAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            RecipeItem.objects.create(
                title=data['title'],
                description=data['description'],
                author=data['author']
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = RecipeAddForm()

    return render(request, html, {"form": form})


def authoradd(request):
    html = "generic_form.html"

    if request.method == "POST":
        form = AuthorAddForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))

    form = AuthorAddForm()
    
    return render(request, html, {'form': form})


def author(request, id):
    author = Author.objects.get(id=id)
    recipe = RecipeItem.objects.filter(author=author)
    return render(request, 'authorinfo.html', {'author': author, 'recipe': recipe})


def recipe(request, id):
    recipe = RecipeItem.objects.get(id=id)
    return render(request, 'recipe.html', {'recipe': recipe})

from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse

from recipe.models import RecipeItem, Author
from recipe.forms import (RecipeAddForm,
                          AuthorAddForm,
                          LoginForm,
                          RecipeEditForm)


def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))


def index(request):
    data = RecipeItem.objects.all()
    return render(request, 'index.html', {'data': data})


@login_required
def add_recipe(request):
    html = "generic_form.html"

    if request.method == "POST":
        form = RecipeAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            RecipeItem.objects.create(
                title=data['title'],
                description=data['description'],
                author=data['author'],
                instructions=data['instructions']
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = RecipeAddForm()

    return render(request, html, {"form": form})


@login_required
def edit_recipe(request, id):
    html = 'generic_form.html'
    recipe_data = RecipeItem.objects.get(id=id)
    if request.user.is_staff or request.user.author == recipe_data.author:
        if request.method == "POST":
            form = RecipeEditForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                recipe_data.title = data['title']
                recipe_data.description = data['description']
                recipe_data.instructions = data['instructions']
                recipe_data.save()
                return HttpResponseRedirect(reverse('homepage'))
    else:
        return HttpResponse('<h1>Page was not found</h1>')

    form = RecipeEditForm(initial={
        'title': recipe_data.title,
        'description': recipe_data.description,
        'instructions': recipe_data.instructions
    })

    return render(request, html, {'recipe_data': recipe_data, 'form': form})


@login_required
def add_author(request):
    html = "generic_form.html"
    if request.user.is_staff:
        if request.method == "POST":
            form = AuthorAddForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                user = User.objects.create_user(username=data['name'], password='asdfasdf2')
                Author.objects.create(
                    name=data['name'],
                    bio=data['bio'],
                    user=user
                )
            return HttpResponseRedirect(reverse('homepage'))
    else:
        return HttpResponse('<h1>Page was not found</h1>')

    form = AuthorAddForm()

    return render(request, html, {'form': form})


def author(request, id):
    author = Author.objects.get(id=id)
    recipe = RecipeItem.objects.filter(author=author)
    return render(request, 'authorinfo.html', {'author': author, 'recipe': recipe})


def recipe(request, id):
    recipe = RecipeItem.objects.get(id=id)
    return render(request, 'recipe.html', {'recipe': recipe})

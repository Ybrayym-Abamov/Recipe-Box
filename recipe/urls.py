from django.urls import path

from recipe import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('author/<int:id>/', views.author),
    path('recipe/<int:id>/', views.recipe),
    path('recipeadd/', views.recipeadd),
    path('authoradd/', views.authoradd)
]

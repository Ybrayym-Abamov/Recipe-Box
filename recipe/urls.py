from django.urls import path

from recipe import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('author/<int:id>/', views.author),
    path('recipe/<int:id>/', views.recipe),
    path('addrecipe/', views.add_recipe),
    path('addauthor/', views.add_author),
    path('login/', views.loginview),
    path('logout/', views.logoutview)
]

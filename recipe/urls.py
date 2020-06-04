from django.urls import path

from recipe import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('author/<int:id>/', views.author),
    path('recipe/<int:id>/', views.recipe, name='recipe'),
    path('addrecipe/', views.add_recipe),
    path('editrecipe/<int:id>/', views.edit_recipe),
    path('favorites/<int:id>/', views.favorites),
    path('addfavorite/<int:id>/', views.add_favorite),
    path('rmfavorite/<int:id>/', views.rm_favorite),
    path('addauthor/', views.add_author),
    path('login/', views.loginview),
    path('logout/', views.logoutview)
]

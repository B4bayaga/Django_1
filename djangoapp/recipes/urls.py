from django.urls import path
from recipes import views


app_name = 'recipe'

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/category/<int:category_id>/',
         views.category, name='category'),
    path('recipes/<slug:slug>/', views.recipe, name='recipe'),
]

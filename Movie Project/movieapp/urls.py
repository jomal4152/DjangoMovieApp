from django.urls import path
from . import views
app_name = 'movieapp'

urlpatterns = [
    path('', views.movielist, name='movielist'),
    path('display/<int:pk>/', views.displaydetails, name='display'),
    path('add/', views.addmovie, name='addmovie'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete')
]

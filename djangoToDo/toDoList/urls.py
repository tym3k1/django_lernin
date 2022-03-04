from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addToDoItem, name='add'),
    path('completed/<todo_id>', views.completedToDoItem, name='completed'),
    path('delete', views.deleteCompleted, name='delete'),
    path('deleteAll', views.deleteAll, name='deleteAll')
]
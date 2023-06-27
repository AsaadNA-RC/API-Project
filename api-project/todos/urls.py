from django.urls import path
from . import views

urlpatterns = [
    path('', views.Todo.as_view(), name='todos-crud'),
    path('<int:id>', views.Todo.as_view(), name='todos-update')
]

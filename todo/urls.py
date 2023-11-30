from django.urls import path
from todo import views
urlpatterns = [
    path('', views.home, name='home'),
    path('todo/add', views.addTask, name='addtask'),
    path('todo/mark_done/<int:pk>', views.mark_done, name='mark_done'),
    path('todo/uncompleted/<int:pk>', views.uncompleted, name='uncompleted'),
    path('todo/edit_task/<int:pk>', views.edit_task, name='edit_task'),
    path('todo/delete_task/<int:pk>', views.delete_task, name='delete_task'),
]
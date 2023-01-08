from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/<int:id>', views.task_view, name='task_view'),
    path('newtask/', views.new_task, name='new_task'),
    path('edit/<int:id>', views.edit_task, name='edit_task'),
    path('changestatus/<int:id>', views.change_status, name='change_status'),
    path('delete/<int:id>', views.delete_task, name='delete_task'),
]
from django.urls import path
from .views import (TaskListView, TaskDetailView, TaskCreateView, 
                    TaskUpdateView, TaskDeleteView, CustomLoginView, 
                    RegisterPageView, TaskReorderView)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPageView.as_view(), name='register'),

    path('', TaskListView.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task'),
    path('task-create/', TaskCreateView.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
    path('task-reorder/', TaskReorderView.as_view(), name='task-reorder'),
]

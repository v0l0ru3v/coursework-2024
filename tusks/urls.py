from django.urls import path
from .views import TusksAPIView, CreateTasks
from . import views

urlpatterns = [
    path('', TusksAPIView.as_view(), name='tusks'),
    # path('', TasksView.as_view(), name='tusks'),
    path('create', CreateTasks.as_view(), name='create'),
    path('<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('<int:pk>/delete', views.TaskDeleteView.as_view(), name='task_delete'),
]
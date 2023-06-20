from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.tusks_home, name='tusks' )
]
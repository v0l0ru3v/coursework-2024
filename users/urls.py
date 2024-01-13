from django.urls import path, include
from users.views import Register
from django.urls import path
from .views import NewsViews
from .models import News
from .views import NewsApi


urlpatterns = [
    path('api/news', NewsApi.as_view(), name='news'),
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('news/', NewsViews.as_view(), name='news')
]
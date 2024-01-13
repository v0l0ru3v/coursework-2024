from django.shortcuts import render, redirect
from django.views import View
from users.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .models import News
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from .serializers import NewsSerializer

class Register(View):
    template_name = 'registration/register.html'

    def get(self,request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context) 
    
    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

class NewsViews(View):
    template_name = 'news.html'
    def get(self, request, *args, **kwargs):
        news = News.objects.all()
        return render(request, 'news.html', {'news': news})

class NewsApiPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10

class NewsApi(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = NewsApiPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from .serializers import TusksSerializer, TusksFilter
from django.views import View
from django.views.generic import DeleteView
from .forms import TuskCreateForm, CommentForm 
from .models import Tusks, User_Tusks, Task_Comment
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend

# class TusksAPIView(generics.ListAPIView):
#     serializer_class = TusksSerializer
#     queryset = Tusks.objects.all()
    

class TusksApiPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10

class TusksAPIView(generics.ListAPIView):
    queryset = Tusks.objects.filter(Q(title__icontains='В') | Q(title__startswith='В'))
    serializer_class = TusksSerializer
    pagination_class = TusksApiPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = TusksFilter

    @action(detail=False, methods=['GET'])
    def custom_filter(self, request, *args, **kwargs):
        title_filter = request.query_params.get('title_filter', 'Веб')
        queryset = Tusks.objects.filter(Q(title__icontains=title_filter))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class CreateTasks(View):
    template_name = 'create.html'
    
    def get(self, request):        
        form1 = TuskCreateForm()
        data = {
            'form1': form1,
        }
        return render(request, self.template_name, data)

    def post(self, request):
        form = TuskCreateForm(request.POST)
        if form.is_valid():
            tasks = form.save()
            ut = User_Tusks(tusks_id=tasks, user_id=request.user)
            ut.save()
            tags = form.cleaned_data['tags']
            for tag in tags:
                tasks.tags.add(tag)
            return redirect('tusks')
        else:
            return redirect('create')

class TaskDeleteView(DeleteView):
     model = Tusks
     template_name = 'task_delete.html'
     success_url = '/tusks/'
     context_object_name = 'task'

def add_comment(request, pk):
    tusk = get_object_or_404(Tusks, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            text_comment = form.cleaned_data['text_comment']
            comment = Task_Comment.objects.create(tusks_id=tusk, text_comment=text_comment)
            return redirect('tusks')
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form})







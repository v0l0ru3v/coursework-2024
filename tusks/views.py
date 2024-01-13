from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from .models import Tusks, User_Tusks,Task_Comment, Tag
from .forms import TuskCreateForm, CommentForm
from django.views.generic import DeleteView
from django.shortcuts import render, get_object_or_404, redirect

class TasksView(View):
    template_name = 'tasks_home.html'
    
    def get(self, request):
        username = request.user
        user_tusks = User_Tusks.objects.filter(user_id__username=username)
        tusks = Tusks.objects.filter(id__in=[ut.tusks_id.id for ut in user_tusks]).order_by('date')    
        return render(request, self.template_name, {'tusks': tusks})


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



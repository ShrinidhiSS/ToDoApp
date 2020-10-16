from django.shortcuts import render

from my_app.models import TodoList
from . import models
from django.views.generic import ListView,CreateView,DeleteView

def home(request):
    return render(request,'base.html')


def todoAdd(request):

    if request.method == 'POST':
        content = request.POST.get('content',None)
        models.TodoList.objects.create(task=content)

    context = {
        'tasks':TodoList.objects.all()
    }
    return render(request,'my_app/todo_form.html',context)

def todoDelete(request,pk):

    pass

# class TaskListView(ListView):
#     model = TodoList
#     template_name='my_app/todo_form.html'
#     context_object_name='tasks'
#     fields = '__all__'




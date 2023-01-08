from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
import datetime

@login_required
def task_list(request):

    search = request.GET.get('search')
    filter = request.GET.get('filter')
    tasks_done_recently = Task.objects.filter(done='done', updated_at__gt=datetime.datetime.now()-datetime.timedelta(days=30), user=request.user).count()
    tasks_done = Task.objects.filter(done='done', user=request.user).count()
    tasks_doing = Task.objects.filter(done='doing', user=request.user).count()

    if search:
        tasks = Task.objects.filter(title__icontains=search, user=request.user)
    elif filter:
        tasks = Task.objects.filter(done=filter, user=request.user)
    else:
        tasks_list = Task.objects.all().order_by('-created_at').filter(user=request.user)
        paginator = Paginator(tasks_list, 6)
        page = request.GET.get('page')
        tasks = paginator.get_page(page)

    return render(request, 'list.html', {'tasks': tasks,
                                         'tasksrecently': tasks_done_recently,
                                         'tasksdone': tasks_done,
                                         'tasksdoing': tasks_doing})

@login_required
def task_view(request, id):
    task = get_object_or_404(Task, pk=id, user=request.user)
    return render(request, 'task.html', {'task': task})

@login_required
def new_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.user = request.user
            task.save()
            
            messages.info(request, 'Tarefa criada com sucesso.')
            return redirect('/')

    else:
        form = TaskForm()
        return render(request, 'addtask.html', {'form': form})

@login_required
def edit_task(request, id):
    task = get_object_or_404(Task, pk=id, user=request.user)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            task.save()
            messages.info(request, 'Tarefa editada com sucesso.')
            return redirect('/')

        else:
            return render(request, 'edittask.html', {'form': form, 'task': task})

    else:
        return render(request, 'edittask.html', {'form': form, 'task': task})

@login_required
def delete_task(request, id):
    task = get_object_or_404(Task, pk=id, user=request.user)
    task.delete()
    messages.info(request, 'Tarefa deletada com sucesso.')
    return redirect('/')

@login_required
def change_status(request, id):
    task = get_object_or_404(Task, pk=id, user=request.user)

    if(task.done == 'doing'):
        task.done = 'done'
    else:
        task.done = 'doing'

    task.save()
    return redirect('/')
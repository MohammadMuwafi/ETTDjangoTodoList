from django.shortcuts import get_object_or_404, render
from todo_app.models import Todo
from django.http import HttpResponseRedirect
from django.urls import is_valid_path, reverse
from .forms import TodoForm


def create_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('todo_app:index'))
    else:
        form = TodoForm()

    context = {
        "form": form,
    }

    return render(request, "todo_app/todo_form.html", context)


def create_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('todo_app:index'))
    else:
        form = TodoForm()

    context = {
        "form": form,
    }

    return render(request, "todo_app/todo_form.html", context)


def index(request):
    context = {
        "todo_list": Todo.objects.all(),
    }
    return render(request, 'todo_app/index.html', context)


def details_for_update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    return render(request, 'todo_app/details_for_update.html', {'todo': todo})


def details_for_delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    return render(request, 'todo_app/details_for_delete.html', {'todo': todo})


def details_for_read(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    return render(request, 'todo_app/details_for_read.html', {'todo': todo})


def details_for_delete_all_todos(request):
    return render(request, 'todo_app/details_for_delete_all_todos.html')


# def create_todo(request):
#     req_title = request.POST['todo_title']
#     req_content = request.POST['todo_content']

#     if req_title == "" or req_title is None:
#         return render(request, 'todo_app/404Error.html')

#     todo = Todo(title=req_title, content=req_content)

#     todo.save()
#     context = {
#         "todo_list": Todo.objects.all(),
#     }
#     return HttpResponseRedirect(reverse('todo_app:index'))


def update_todo(request):
    todo = get_object_or_404(Todo, pk=int(request.POST['todo_id']))

    req_title = request.POST['todo_title']
    req_content = request.POST['todo_content']
    if req_title == "" or req_title is None:
        return render(request, 'todo_app/404Error.html')

    todo.title = request.POST['todo_title']
    todo.content = request.POST['todo_content']
    todo.save()
    context = {
        "todo_list": Todo.objects.all(),
    }
    return HttpResponseRedirect(reverse('todo_app:index'))


def delete_todo(request):
    todo = get_object_or_404(Todo, pk=int(request.POST['todo_id']))

    if todo is None:
        return render(request, 'todo_app/404Error.html')

    Todo.objects.filter(id=int(request.POST['todo_id'])).delete()
    return HttpResponseRedirect(reverse('todo_app:index'))


def read_todo(request):
    return HttpResponseRedirect(reverse('todo_app:index'))


def delete_all_todos(request):
    Todo.objects.all().delete()
    return HttpResponseRedirect(reverse('todo_app:index'))


def search_todo(request):
    search_value = request.GET['search-bar']
    # for exact title ==> Todo.objects.all().filter(title=search_value),
    context = {
        "todo_list": Todo.objects.all().filter(title__contains=search_value)
    }
    return render(request, "todo_app/index.html", context)

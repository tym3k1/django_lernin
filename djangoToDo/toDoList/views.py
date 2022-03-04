from django.shortcuts import redirect, render


from .models import toDoList
from .forms import ToDoListForm

from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    todo_items = toDoList.objects.order_by('id')
    form = ToDoListForm()
    context = {'todo_items' : todo_items, 'form' : form}
    return render(request, 'toDoList/index.html', context)

@require_POST
def addToDoItem(request):
    form = ToDoListForm(request.POST)
    if form.is_valid:
        new_todo = toDoList(text = request.POST['text'])
        new_todo.save()
    return redirect('index')

def completedToDoItem(request, todo_id):
    todo = toDoList.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()

    return redirect('index')


def deleteCompleted(request):
    toDoList.objects.filter(completed__exact=True).delete()

    return redirect('index')

def deleteAll(request):
    toDoList.objects.all().delete()

    return redirect('index')
from django.shortcuts import render,redirect

from .models import Task, Person
from .forms import TaskForm, PersonForm

def home(request):
    tasks = Task.objects.all()
    persons = Person.objects.all()
    return render(request, 'home.html', {'tasks':tasks,'persons' : persons})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = TaskForm()
    return render(request, 'taskFormulario.html',{'form':form})
def add_person(request):

    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PersonForm()

    return render(request, 'personFormulario.html', {'form': form})
def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()  # Esto guarda la tarea actualizada en la base de datos
            return redirect('ruta_de_la_vista')  # Redirecciona a la página deseada después de actualizar
    else:
        form = TaskForm(instance=task)
    return render(request, 'taskFormulario.html', {'form': form})

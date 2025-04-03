from django.shortcuts import render
from .models import Tarea
def home(request):
    tareas=Tarea.objects.all()
    context={"tareas":tareas}
    return render(request,"todo/home.html",context)
def agregar(request):
    if request.method =="POST":
        form=tareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form=tareaform()
        


# Create your views here.

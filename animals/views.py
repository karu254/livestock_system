from django.shortcuts import render, redirect, get_object_or_404
from .models import Animal
from .forms import AnimalForm   
from django.contrib.auth.decorators import login_required   

# Create your views here.
@login_required
def index(request):
    animals = Animal.objects.all() # Retrieve all animals from the database
    return render(request, 'animals/index.html', {'animals': animals})

@login_required
def add_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            animal = form.save(commit=False)
            animal.created_by = request.user # Track who added the record
            animal.save()
            return redirect('animals_home')
    else:
        form = AnimalForm()
    return render(request, 'animals/add_animal.html', {'form': form})


@login_required
def animal_details(request, id):
    animal = get_object_or_404(Animal, id=id)
    return render(request, 'animals/animal_details.html', {'animal': animal})

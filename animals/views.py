from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Animal
from .forms import AnimalForm

@login_required
def animals_list(request):
    animals = Animal.objects.filter(is_active=True).order_by('date_of_birth')
    return render(request, 'animals/animals_list.html', {'animals': animals})

@login_required
def add_animal(request):
    if request.method == 'POST': # Form was submitted
        form = AnimalForm(request.POST)
        if form.is_valid():
            animal = form.save(commit=False) # Don't save to database yet
            animal.added_by = request.user
            animal.save() # Now save
            return redirect('animal_list') # Redirect to list of animals
    else:
        form = AnimalForm()
    return render(request, 'animals/animal_form.html', {'form': form})

@login_required
def animal_detail(request, pk): # pk is the primary key of the animal
    animal = get_object_or_404(Animal, pk=pk) # Get animal by primary key
    return render(request, 'animals/animal_detail.html', {'animal': animal}) # Pass animal to template


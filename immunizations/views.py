from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Immunization, ImmunizationSchedule
from .forms import ImmunizationForm, ImmunizationScheduleForm

@login_required
def immunization_list(request):
    immunizations = Immunization.objects.all()
    return render(request, 'immunizations/immunization_list.html', {'immunizations': immunizations})

@login_required
def add_immunization(request):
    if request.method == 'POST':
        form = ImmunizationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('immunization_list')
    else:
        form = ImmunizationForm()
    return render(request, 'immunizations/add_immunization.html', {'form': form})

@login_required
def schedule_list(request):
    schedules = ImmunizationSchedule.objects.select_related('animal', 'immunization').all()
    return render(request, 'immunizations/schedule_list.html', {'schedules': schedules})

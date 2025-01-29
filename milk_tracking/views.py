from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import MilkRecord
from .forms import MilkRecordForm
from django.utils.timezone import now, timedelta


@login_required
def milk_list(request):
    if request.user.is_staff:  # Admin can view all records
        records = MilkRecord.objects.all()
    else:  # Users can only see records for the past 2 days
        cutoff_date = now() - timedelta(days=2)
        records = MilkRecord.objects.filter(date__gte=cutoff_date)
    return render(request, 'milk_tracking/milk_list.html', {'records': records})

@login_required
def add_milk_record(request):
    if request.method == 'POST':
        form = MilkRecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.recorded_by = request.user
            record.save()
            return redirect('milk_list')
    else:
        form = MilkRecordForm()
    return render(request, 'milk_tracking/milk_form.html', {'form': form})

@login_required
def milk_records(request):
    # Fetch all milk production records
    milk_data = MilkRecord.objects.all().order_by('-date')  # Order by most recent date

    context = {
        'milk_data': milk_data
    }

    return render(request, 'milk/milk_records.html', context)

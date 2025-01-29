from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import SalesRecord, ProductType
from .forms import SalesRecordForm, ProductTypeForm

@login_required
def add_sales_record(request):
    if request.method == 'POST':
        form = SalesRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sales_list')
    else:
        form = SalesRecordForm()
    return render(request, 'sales/sales_form.html', {'form': form})

@login_required
def sales_list(request):
    sales_records = SalesRecord.objects.all()
    return render(request, 'sales/sales_list.html', {'sales_records': sales_records})

@login_required
def sales_report(request):
    daily_sales = SalesRecord.objects.filter(date__day=request.GET.get('day', None))
    monthly_sales = SalesRecord.objects.filter(date__month=request.GET.get('month', None))
    yearly_sales = SalesRecord.objects.filter(date__year=request.GET.get('year', None))
    return render(request, 'sales/sales_report.html', {
        'daily_sales': daily_sales,
        'monthly_sales': monthly_sales,
        'yearly_sales': yearly_sales,
    })

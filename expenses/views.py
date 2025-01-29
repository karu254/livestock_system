from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ExpenseRecord, ExpenseCategory
from .forms import ExpenseRecordForm, ExpenseCategoryForm

@login_required
def add_expense_record(request):
    if request.method == 'POST':
        form = ExpenseRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseRecordForm()
    return render(request, 'expenses/expense_form.html', {'form': form})

@login_required
def expense_list(request):
    expenses = ExpenseRecord.objects.all()
    return render(request, 'expenses/expense_list.html', {'expenses': expenses})

@login_required
def expense_report(request):
    daily_expenses = ExpenseRecord.objects.filter(date__day=request.GET.get('day', None))
    monthly_expenses = ExpenseRecord.objects.filter(date__month=request.GET.get('month', None))
    yearly_expenses = ExpenseRecord.objects.filter(date__year=request.GET.get('year', None))
    return render(request, 'expenses/expense_report.html', {
        'daily_expenses': daily_expenses,
        'monthly_expenses': monthly_expenses,
        'yearly_expenses': yearly_expenses,
    })

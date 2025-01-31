from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from milk_tracking.models import MilkRecord
from sales.models import Sale
from expenses.models import ExpenseRecord
from animals.models import Animal
import datetime
import json
from . import models
from django.db.models import Sum

#test 
def is_admin(user):
    return user.is_superuser or user.role == "admin"

def is_regular_user(user):
    return user.role == "user"

@login_required
@user_passes_test(is_regular_user)
def profile(request):
    return render(request, "accounts/profile.html")


@login_required
@user_passes_test(is_admin) # Only admin can access this view
def dashboard_home(request):
    # Get daily milk production
    today = datetime.date.today()
    daily_milk = MilkRecord.objects.filter(date=today).aggregate(total_milk=Sum('milk_quantity'))['total_milk'] or 0

    # Get total expenses and sales for today
    daily_expense = ExpenseRecord.objects.filter(date=today).aggregate(total=Sum('amount'))['total'] or 0
    daily_sales = Sale.objects.filter(date=today).aggregate(total=Sum('amount'))['total'] or 0

    # Count animals by category
    total_animals = Animal.objects.count()
    pregnant_animals = Animal.objects.filter(is_active=True, stage='Pregnant').count()
    male_animals = Animal.objects.filter(gender='Male').count()
    female_animals = Animal.objects.filter(gender='Female').count()

    context = {
        'daily_milk': daily_milk,
        'daily_expense': daily_expense,
        'daily_sales': daily_sales,
        'total_animals': total_animals,
        'pregnant_animals': pregnant_animals,
        'male_animals': male_animals,
        'female_animals': female_animals,
    }
    return render(request, 'dashboard/dashboard_home.html', context)

@login_required
def reports(request):
    # Data for charts
    daily_sales = list(Sale.objects.values('date').annotate(total=Sum('amount')))
    daily_expenses = list(ExpenseRecord.objects.values('date').annotate(total=Sum('amount')))
    daily_milk = list(MilkRecord.objects.values('date').annotate(total=Sum('milk_quantity')))

    context = {
        'daily_sales': json.dumps(daily_sales),
        'daily_expenses': json.dumps(daily_expenses),
        'daily_milk': json.dumps(daily_milk),
    }
    return render(request, 'dashboard/reports.html', context)

def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html')


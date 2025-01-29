from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from milk_tracking.models import MilkRecord
from animals.models import Animal
from django.db.models import Sum, Avg, Count
from datetime import date, timedelta

@login_required
def reports_dashboard(request):
    # Calculate summaries
    total_milk = MilkRecord.objects.aggregate(Sum('milk_quantity'))['milk_quantity__sum'] or 0
    average_milk = MilkRecord.objects.aggregate(Avg('milk_quantity'))['milk_quantity__avg'] or 0
    total_cows = Animal.objects.count()
    cows_by_gender = Animal.objects.values('gender').annotate(count=Count('id'))
    age_groups = Animal.objects.values('age_group').annotate(count=Count('id'))

    # Generate a daily milk production trend (last 7 days)
    today = date.today()
    last_7_days = [(today - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(6, -1, -1)]
    daily_trend = [
        MilkRecord.objects.filter(date=day).aggregate(Sum('milk_quantity'))['milk_quantity__sum'] or 0
        for day in last_7_days
    ]

    context = {
        'total_milk': total_milk,
        'average_milk': average_milk,
        'total_cows': total_cows,
        'cows_by_gender': cows_by_gender,
        'age_groups': age_groups,
        'last_7_days': last_7_days,
        'daily_trend': daily_trend,
    }
    return render(request, 'reports/reports_dashboard.html', context)

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import FeedRecord, FeedType
from .forms import FeedRecordForm, FeedTypeForm
from animals.models import Animal

@login_required
def add_feed_record(request):
    if request.method == 'POST':
        form = FeedRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feed_list')
    else:
        form = FeedRecordForm()
    return render(request, 'feed_management/feed_form.html', {'form': form})

@login_required
def feed_list(request):
    feed_records = FeedRecord.objects.all()
    return render(request, 'feed_management/feed_list.html', {'feed_records': feed_records})

@login_required
def add_feed_type(request):
    if request.method == 'POST':
        form = FeedTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feed_suggestions')
    else:
        form = FeedTypeForm()
    return render(request, 'feed_management/feed_form.html', {'form': form})

@login_required
def feed_suggestions(request):
    age_groups = Animal.objects.values('age_group').distinct()
    feed_types = FeedType.objects.all()
    return render(request, 'feed_management/feed_suggestions.html', {'age_groups': age_groups, 'feed_types': feed_types})

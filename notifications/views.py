from django.shortcuts import render, redirect, get_object_or_404
from .models import Notification
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.utils.timezone import now
from django.contrib.auth.models import User
#new feature
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

@login_required
def notification_list(request):
    notifications = Notification.objects.filter(is_resolved=False).order_by('due_date')
    return render(request, 'notifications/notification_list.html', {'notifications': notifications})

@login_required
def resolve_notification(request, id):
    notification = get_object_or_404(Notification, id=id)
    if request.user.is_staff:  # Only admin can resolve
        notification.is_resolved = True
        notification.save()
    return redirect('notification_list')

@login_required
def send_email_notifications():
    # Fetch notifications for today
    today_notifications = Notification.objects.filter(
        due_date__exact=now().date(),
        is_resolved=False
    )

    if today_notifications.exists():
        subject = "Today's Notifications"
        message = "Here are the events for today:\n\n"
        for n in today_notifications:
            message += f"- {n.event_type} for {n.animal.tag_number}: {n.message}\n"

        # Send to all users
        users = User.objects.all()
        recipients = [user.email for user in users if user.email]
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipients)

    return None

#new feature
@login_required
def notification_list(request):
    filter_type = request.GET.get('filter_type', '')
    notifications = Notification.objects.filter(is_resolved=False).order_by('due_date')
    
    #Apply filter if specified
    if filter_type:
        notifications = notifications.filter(event_type=filter_type)

    #Pagination setup
    paginator = Paginator(notifications, 10) # Show 10 notifications per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'notifications/notification_list.html', {
        'notifications': page_obj, 
        'filter_type': filter_type
    })

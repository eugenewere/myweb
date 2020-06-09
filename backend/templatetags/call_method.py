from itertools import count

from django import template
from django.db.models import Count

from backend.models import *
# from humanize import  naturaltime
from django.contrib.humanize.templatetags.humanize import naturaltime



register = template.Library()
@register.filter(name='social_ac')
def get_social_accounts(request):
    return SocialMedia.objects.all()

@register.filter(name='get_layout_notifications_email')
def get_layout_notifications_email(request):
    names_list = []
    names = ContactUs.objects.filter(status="UNREAD").order_by("-created_at")
    for name in names:
        names_list.append(name.email)
    return set(names_list)

@register.filter(name='get_layout_notifications_email_count')
def get_layout_notifications_email_count(request):
    names_list = []
    names = ContactUs.objects.filter(status="UNREAD").order_by("-created_at")
    for name in names:
        names_list.append(name.email)

    return set(names_list)



@register.filter(name='admin')
def get_user_accounts(request):
    admin= Admin.objects.filter(user_ptr_id = request.user.id).first()
    if admin:
        url =admin.admin_profile.url
    else:
        url = ''

    return url


@register.filter(name='message_names')
def get_user_names(request, email):
    user = ContactUs.objects.filter(email=email).first()
    return user.first_name + " " + user.last_name

@register.filter(name='last_message')
def get_user_last_message(request, email):
    message = ContactUs.objects.filter(email=email).values_list("message", flat=True).last()
    return message
@register.filter(name='messages_status')
def get_user_messages_status(request, email):
    message = ContactUs.objects.filter(email=email).filter(status="UNREAD")
    if message:
        return True
    return False


@register.filter(name='last_message_time')
def get_user_last_message_time(request, email):
    message = ContactUs.objects.filter(email=email).values_list("created_at", flat=True).last()
    return naturaltime(message)

@register.filter(name='get_messages')
def get_messages(request, email):
    messages = ContactUs.objects.filter(email=email).all()
    return messages




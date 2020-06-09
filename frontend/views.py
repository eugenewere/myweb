from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from backend.models import *
from backend.forms import *


def home(request):

    context={
        'announces': AnnouncementBar.objects.filter(status='SHOW'),
        'carousels': Carousel.objects.all(),
        'about': About.objects.first(),
        'categories': Category.objects.all(),
        'hobbies': Hobbies.objects.all(),
        'services': Speciality.objects.all(),
        "pcs": Progresscounter.objects.first(),
        "pro_done": Portfolio.objects.filter(category__name__contains="Web").count(),
        "logo_done": Portfolio.objects.filter(category__name__contains="Logo Design").count(),
        "participations":WorkParticipation.objects.order_by("-created_at"),
        "expertise": Expertise.objects.all(),
        "projects": Portfolio.objects.all(),
        "counter_image": CounterImages.objects.filter(status="ACTIVE").first(),
        "expertise_image": WorkExpertise.objects.filter(status="ACTIVE").first(),
        "available_image": AvailableForTheProject.objects.filter(status="ACTIVE").first(),
        "contuctus_image": ContactMeImage.objects.filter(status="ACTIVE").first(),
        "sendmsgs_image": SendMessageImage.objects.filter(status="ACTIVE").first(),

    }
    return render(request, 'home/index.html', context)


def portfolio(request):
    context = {
        'announces': AnnouncementBar.objects.filter(status='SHOW'),
    }
    return render(request, 'portfolios/portfolio.html', context)

@csrf_exempt
def addmessage(request):
    if request.method == "POST":
        print(request.POST)
        form = MessageForm(request.POST)
        print(form)

        if form.is_valid():
            form.save()

            return JsonResponse(
                {
                    'results': 'success',
                    'form_success': "Successfuly Sent The Message",
                },
                safe=False)
        else:
            return JsonResponse(
                {'results': 'error',
                 'form_error': "Message not sent please"},
                safe=False)
    return redirect('frontend:home')


def addsubscribers(request):
    if request.method == "POST":
        print(request.POST)
        form = NewsLetterForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return JsonResponse(
                {
                    'results': 'success',
                    'form_success': "Successfuly Subscribed",
                },
                safe=False)
        else:
            return JsonResponse(
                {'results': 'error',
                 'form_error': "Unable to Subscribe"},
                safe=False)
    return redirect('frontend:home')


def view_cv(request):
    context={
        'admin': Admin.objects.all().first(),
        'categories': Category.objects.all(),
        'about':About.objects.all().first(),
        'social': SocialMedia.objects.all(),
    }
    return render(request, 'cv/cv.html', context)
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render, redirect
import sweetify
from mysite.settings import *
from django.contrib.auth import login as auth_login
# # Base method with no type specified
# sweetify.sweetalert(self.request, 'Westworld is awesome', text='Really... if you have the chance - watch it!' persistent='I agree!')
#
# # Additional methods with the type already defined
# sweetify.info(self.request, 'Message sent', button='Ok', timer=3000)
# sweetify.success(self.request, 'You successfully changed your password')
# sweetify.error(self.request, 'Some error happened here - reload the site', persistent=':(')
# sweetify.warning(self.request, 'This is a warning... I guess')
# Create your views here.
from backend.forms import *
from backend.models import *
# 70961e4ea8d0fa4fbaeb2b617ce45474c58af948da6c102406d7c631aa4d41b7


login_required()
def home(request):
    messages_count = ContactUs.objects.all().count()
    unread_messages_count = ContactUs.objects.filter(status='UNREAD').count()
    read_messages_count = ContactUs.objects.filter(status='READ').count()
    portfolio_count = Portfolio.objects.filter(status='DONE').count()
    undone_portfolio_count = Portfolio.objects.filter(status='COOMINGSOON').count()
    context={
        "messages_count": messages_count,
        "unread_messages_count":unread_messages_count,
        "read_messages_count":read_messages_count,
        'p_count':portfolio_count,
        'undone_portfolio_count':undone_portfolio_count,
    }
    return render(request, 'PurpleAdmin-Free-Admin-Template/index.html', context)


login_required()
def category(request):
    categories = Category.objects.all()
    context = {
        "categories": categories,
    }
    return render(request, 'PurpleAdmin-Free-Admin-Template/category/category.html', context)


def addcategory(request):
    if request.method == 'POST':
        k = request.POST.get('name')
        form = CategoryForm(request.POST)
        print(form)
        if form.is_valid():
            if not Category.objects.filter(name__exact=k):
                form.save()
                sweetify.success(request, 'You successfully added a category')
            else:
                sweetify.error(request, 'Seams the category exists', persistent=':(')
        else:
            sweetify.error(request, 'Error adding category', persistent=':(')

    return redirect('backend:category')


def deletecategory(request, category_id):
    category = Category.objects.filter(id=category_id)
    if category:
        category.delete()
        sweetify.success(request, 'You successfully deleted a category')
    else:
        sweetify.error(request, 'Error deleting category', persistent=':(')
        return redirect('backend:category')
    return redirect('backend:category')


def editcategory(request, category_id):
    category = Category.objects.filter(id=category_id).first()
    categoryform = CategoryForm(request.POST, instance=category)
    if categoryform.is_valid():
        categoryform.save()
        sweetify.success(request, 'You successfully edited a category')
    else:
        sweetify.error(request, 'Error deleting category', persistent=':(')
    return redirect('backend:category')


login_required()
def view_carousel(request):
    context = {
        "carousels": Carousel.objects.all()
    }
    return render(request, 'PurpleAdmin-Free-Admin-Template/carousel/carousel2.html', context)


def addcarousel(request):
    if request.method == 'POST':
        carouselForm = CarouselImageForm(request.POST, request.FILES)
        if carouselForm.is_valid():
            carouselForm.save()
            sweetify.success(request, 'Carousel Image Added Successfully')
            return redirect('backend:view_carousel')
        else:
            sweetify.error(request, 'Carousel Image not Added ')
            return redirect('backend:view_carousel')
    return redirect('backend:view_carousel')


def carousel_delete(request, carousel_id):
    carousel = Carousel.objects.filter(id=carousel_id).first()
    carousel.image.delete()
    carousel.delete()
    sweetify.success(request, 'Carousel Image Deleted Succesfully')

    return redirect('backend:view_carousel')


def carousel_edit(request, carousel_id):
    carousel = Carousel.objects.filter(id=carousel_id).first()
    form = CarouselImageForm(request.POST, request.FILES, instance=carousel)
    if form.is_valid():
        form.save()
        sweetify.success(request, 'Carousel Image Updated Succesfully')

    return redirect('backend:view_carousel')


login_required()


def about_me(request):
    abouts = About.objects.all()
    context = {
        'abouts': abouts,
        'categories': Category.objects.all(),
    }
    return render(request, 'PurpleAdmin-Free-Admin-Template/about/about.html', context)


def addabout_me(request):
    if request.method == 'POST':
        aboutmeForm = AboutMeForm(request.POST, request.FILES)
        print(aboutmeForm)
        if aboutmeForm.is_valid():
            if not About.objects.count() > 1:
                aboutmeForm.save()
                sweetify.success(request, 'Data added Successfully')
            else:
                sweetify.error(request, 'Data Already exists')
            return redirect('backend:about_me')
        else:
            sweetify.error(request, 'Data not Added ')
            return redirect('backend:about_me')
    return redirect('backend:about_me')


def editabout_me(request, about_id):
    about = About.objects.filter(id=about_id).first()
    if request.method == 'POST':
        aboutmeForm = AboutMeForm(request.POST, request.FILES, instance=about)
        print(aboutmeForm)
        if aboutmeForm.is_valid():
            aboutmeForm.save()
            sweetify.success(request, 'Data updated Successfully')
            return redirect('backend:about_me')
        else:
            sweetify.error(request, 'Data not updated ')
            return redirect('backend:about_me')
    return redirect('backend:about_me')


def deleteabout_me(request, about_id):
    about = About.objects.filter(id=about_id).first()
    if about:
        about.delete()
        sweetify.success(request, 'About Me Deleted Succesfully')
    else:
        sweetify.error(request, 'Error deleting About')
    return redirect('backend:about_me')


login_required()


def hobbies(request):
    context = {
        'hobbies': Hobbies.objects.order_by('?')
    }
    return render(request, 'PurpleAdmin-Free-Admin-Template/hobby/hobbies.html', context)


def addhobbies(request):
    if request.method == 'POST':
        hobbiesForm = HobbiesForm(request.POST)
        print(hobbiesForm)
        if hobbiesForm.is_valid():
            hobbiesForm.save()
            sweetify.success(request, 'Hobbies added Successfully')

            return redirect('backend:hobbies')
        else:
            sweetify.error(request, 'Hobbies not Added ')
            return redirect('backend:hobbies')
    return redirect('backend:hobbies')


def edithobbies(request, hobby_id):
    hobby = Hobbies.objects.filter(id=hobby_id).first()
    if request.method == 'POST':
        hobbiesForm = HobbiesForm(request.POST, instance=hobby)
        print(hobbiesForm)
        if hobbiesForm.is_valid():
            if not About.objects.count() > 1:
                hobbiesForm.save()
                sweetify.success(request, 'Hobbies added Successfully')
            else:
                sweetify.error(request, 'Hobbies Already exists')
            return redirect('backend:hobbies')
        else:
            sweetify.error(request, 'Hobbies not Added ')
            return redirect('backend:hobbies')
    return redirect('backend:hobbies')


def deletehobbies(request, hobby_id):
    about = Hobbies.objects.filter(id=hobby_id).first()
    if about:
        about.delete()
        sweetify.success(request, 'Hobby Deleted Succesfully')
    else:
        sweetify.error(request, 'Error deleting Hobby')
    return redirect('backend:hobbies')


login_required()


def services(request):
    context = {
        'services': Speciality.objects.all()
    }
    return render(request, 'PurpleAdmin-Free-Admin-Template/services/services.html', context)


def addservices(request):
    if request.method == 'POST':
        serviceForm = ServicesForm(request.POST)
        print(serviceForm)
        if serviceForm.is_valid():
            serviceForm.save()
            sweetify.success(request, 'Services added Successfully')

            return redirect('backend:services')
        else:
            sweetify.error(request, 'Services not Added ')
            return redirect('backend:services')
    return redirect('backend:services')


def editservices(request, service_id):
    speciality = Speciality.objects.filter(id=service_id).first()
    if request.method == 'POST':
        serviceForm = ServicesForm(request.POST, instance=speciality)
        print(serviceForm)
        if serviceForm.is_valid():
            serviceForm.save()
            sweetify.success(request, 'Services Updated Successfully')
            return redirect('backend:services')
        else:
            sweetify.error(request, 'Services not Updated ')
            return redirect('backend:services')

    return redirect('backend:services')


def deleteservices(request, service_id):
    speciality = Speciality.objects.filter(id=service_id).first()
    if speciality:
        speciality.delete()
        sweetify.success(request, 'Service Deleted Succesfully')
    else:
        sweetify.error(request, 'Error deleting Service')
    return redirect('backend:services')


login_required()


def progresscounter(request):
    context = {
        "pcs": Progresscounter.objects.all(),
        "pro_done": Portfolio.objects.filter(category__name__contains="Web").count(),
        "logo_done": Portfolio.objects.filter(category__name__contains="Logo Design").count(),
    }
    return render(request, 'PurpleAdmin-Free-Admin-Template/progress/progress.html', context)


def addprogresscounter(request):
    if request.method == 'POST':
        serviceForm = ProgressForm(request.POST)
        print(serviceForm)
        if serviceForm.is_valid():
            serviceForm.save()
            sweetify.success(request, 'Progress Counter Data added Successfully')
        else:
            sweetify.error(request, 'Progress Counter Data not Added ')
    return redirect("backend:progresscounter")


def editprogresscounter(request, pc_id):
    specialityy = Progresscounter.objects.filter(id=pc_id).first()
    if request.method == 'POST':
        serviceform = ServicesForm(request.POST, instance=specialityy)
        print(serviceform)
        if serviceform.is_valid():
            serviceform.save()
            sweetify.success(request, 'Progress Updated Successfully')
        else:
            sweetify.error(request, 'Progress not Updated ')
    return redirect("backend:progresscounter")


def deleteprogresscounter(request, pc_id):
    specialityy = Progresscounter.objects.filter(id=pc_id).first()
    if specialityy:
        specialityy.delete()
        sweetify.success(request, 'Progress Deleted Succesfully')
    else:
        sweetify.error(request, 'Error deleting Progress')
    return redirect("backend:progresscounter")


login_required()


def counterimages(request):
    context = {
        'images': CounterImages.objects.all()
    }
    return render(request, 'PurpleAdmin-Free-Admin-Template/images/counterImages.html', context)


def addcounterimages(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        counterImageForm = CounterImageForm(request.FILES, request.FILES)
        print(image)
        if counterImageForm.is_valid():
            CounterImages.objects.create(
                image=image,
            )
            sweetify.success(request, 'Counter Image added Successfully')

            return redirect('backend:counterimages')
        else:
            sweetify.error(request, 'Counter Image not Added ')
            return redirect('backend:counterimages')
    return redirect('backend:counterimages')


def editcounterimages(request, counter_image_id):
    counter = CounterImages.objects.filter(id=counter_image_id).first()
    if request.method == 'POST':
        counterImageForm = CounterImageForm(request.POST, request.FILES, instance=counter)
        print(counterImageForm)
        if counterImageForm.is_valid():
            counterImageForm.save()
            sweetify.success(request, 'Counter Image Updated Successfully')

            return redirect('backend:counterimages')
        else:
            sweetify.error(request, 'Counter Image not Updated ')
            return redirect('backend:counterimages')
    return redirect('backend:counterimages')


def deletecounterimages(request, counter_image_id):
    counter = CounterImages.objects.filter(id=counter_image_id).first()
    if counter:
        counter.image.delete()
        counter.delete()
        sweetify.success(request, 'Counter Deleted Succesfully')
        return redirect('backend:counterimages')

    else:
        sweetify.error(request, 'Error deleting Counter')
        return redirect('backend:counterimages')


def editcounterimagesstatus(request, counter_image_id):
    counter = CounterImages.objects.filter(id=counter_image_id).first()
    if counter.status == "ACTIVE":

        CounterImages.objects.filter(id=counter.id).update(
            status="INACTIVE",
        )
        sweetify.success(request, 'Counter Image Status Updated Successfully')

    elif counter.status == "INACTIVE":
        CounterImages.objects.exclude(id=counter.id).update(
            status="INACTIVE",
        )
        CounterImages.objects.filter(id=counter.id).update(
            status="ACTIVE",
        )
        sweetify.error(request, 'Counter Image Status Updated Successfully')
    return redirect("backend:counterimages")


login_required()


def workexpertimage(request):
    context = {
        'images': WorkExpertise.objects.all()
    }
    return render(request, 'PurpleAdmin-Free-Admin-Template/images/workexpimage.html', context)


def addworkexpertimage(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        workexpertForm = WorkExpImageForm(request.FILES, request.FILES)
        print(image)
        if workexpertForm.is_valid():
            WorkExpertise.objects.create(
                image=image,
            )
            sweetify.success(request, 'Work Expert Image added Successfully')
            return redirect('backend:workexpertimage')
        else:
            sweetify.error(request, 'Work Expert Image not Added ')
            return redirect('backend:workexpertimage')
    return redirect('backend:workexpertimage')


def editworkexpertimage(request, workexpertimage_id):
    counter = WorkExpertise.objects.filter(id=workexpertimage_id).first()
    if request.method == 'POST':
        counterImageForm = WorkExpImageForm(request.POST, request.FILES, instance=counter)
        print(counterImageForm)
        if counterImageForm.is_valid():

            counterImageForm.save()
            sweetify.success(request, 'Work Expert Image Updated Successfully')
            return redirect('backend:workexpertimage')
        else:
            sweetify.error(request, 'Work Expert Image not Updated ')
            return redirect('backend:workexpertimage')
    return redirect('backend:workexpertimage')


def deleteworkexpertimage(request, workexpertimage_id):
    counter = WorkExpertise.objects.filter(id=workexpertimage_id).first()
    if counter:
        counter.image.delete()
        counter.delete()
        sweetify.success(request, 'Work Expert Image Deleted Succesfully')
        return redirect('backend:workexpertimage')

    else:
        sweetify.error(request, 'Error deleting Work Expert Image')
        return redirect('backend:workexpertimage')


def editworkexpertimagestatus(request, workexpertimage_id):
    counter = WorkExpertise.objects.filter(id=workexpertimage_id).first()
    if counter.status == "ACTIVE":

        WorkExpertise.objects.filter(id=counter.id).update(
            status="INACTIVE",
        )
        sweetify.success(request, 'Work Expert Image Status Updated Successfully')

    elif counter.status == "INACTIVE":
        WorkExpertise.objects.exclude(id=counter.id).update(
            status="INACTIVE",
        )
        WorkExpertise.objects.filter(id=counter.id).update(
            status="ACTIVE",
        )
        sweetify.error(request, 'Work Expert Image Status Updated Successfully')
    return redirect('backend:workexpertimage')


login_required()


def availforprojimage(request):
    contxt = {
        "images": AvailableForTheProject.objects.all()
    }
    return render(request, "PurpleAdmin-Free-Admin-Template/images/availablefortheprojectimage.html", contxt)


def addavailforprojimage(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        workexpertForm = AvailableForTheProjectImageForm(request.FILES, request.FILES)
        print(image)
        if workexpertForm.is_valid():
            AvailableForTheProject.objects.create(
                image=image,
            )
            sweetify.success(request, 'Available for the project Image added Successfully')
            return redirect('backend:availforprojimage')
        else:
            sweetify.error(request, 'Available for the project Image not Added ')
            return redirect('backend:availforprojimage')
    return redirect('backend:availforprojimage')


def deleteavailforprojimage(request, availforprojimage_id):
    counter = AvailableForTheProject.objects.filter(id=availforprojimage_id).first()
    if counter:
        counter.image.delete()
        counter.delete()
        sweetify.success(request, 'Available for the project Image Deleted Succesfully')
        return redirect('backend:availforprojimage')

    else:
        sweetify.error(request, 'Error deleting Available for the project')
        return redirect('backend:availforprojimage')


def editavailforprojimage(request, availforprojimage_id):
    counter = AvailableForTheProject.objects.filter(id=availforprojimage_id).first()
    if request.method == 'POST':
        counterImageForm = AvailableForTheProjectImageForm(request.POST, request.FILES, instance=counter)
        print(counterImageForm)
        if counterImageForm.is_valid():

            counterImageForm.save()
            sweetify.success(request, 'Available for the project Updated Successfully')

        else:
            sweetify.error(request, 'Available for the project not Updated ')

    return redirect('backend:availforprojimage')


def editavailforprojimagestatus(request, availforprojimage_id):
    counter = AvailableForTheProject.objects.filter(id=availforprojimage_id).first()
    if counter.status == "ACTIVE":

        AvailableForTheProject.objects.filter(id=counter.id).update(
            status="INACTIVE",
        )
        sweetify.success(request, 'Work Expert Image Status Updated Successfully')

    elif counter.status == "INACTIVE":
        AvailableForTheProject.objects.exclude(id=counter.id).update(
            status="INACTIVE",
        )
        AvailableForTheProject.objects.filter(id=counter.id).update(
            status="ACTIVE",
        )
        sweetify.error(request, 'Work Expert Image Status Updated Successfully')
    return redirect('backend:availforprojimage')


login_required()


def contactmeimage(request):
    contxt = {
        "images": ContactMeImage.objects.all()
    }
    return render(request, "PurpleAdmin-Free-Admin-Template/images/contactmeiamge.html", contxt)


def addcontactmeimage(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        workexpertForm = ContactMeImageForm(request.FILES, request.FILES)
        print(image)
        if workexpertForm.is_valid():
            ContactMeImage.objects.create(
                image=image,
            )
            sweetify.success(request, 'Contact Me Image Image added Successfully')
        else:
            sweetify.error(request, 'Contact Me Image Image not Added ')

    return redirect('backend:contactmeimage')


def editcontactmeimage(request, contactmeimage_id):
    counter = ContactMeImage.objects.filter(id=contactmeimage_id).first()
    if request.method == 'POST':
        counterImageForm = ContactMeImageForm(request.POST, request.FILES, instance=counter)
        print(counterImageForm)
        if counterImageForm.is_valid():

            counterImageForm.save()
            sweetify.success(request, 'Contact Me Image Updated Successfully')

        else:
            sweetify.error(request, 'Contact Me Image not Updated ')
    return redirect('backend:contactmeimage')


def deletecontactmeimage(request, contactmeimage_id):
    counter = ContactMeImage.objects.filter(id=contactmeimage_id).first()
    if counter:
        counter.image.delete()
        counter.delete()
        sweetify.success(request, 'Contact Me Image Image Deleted Succesfully')
        return redirect('backend:contactmeimage')

    else:
        sweetify.error(request, 'Error deleting Contact Me Image')
        return redirect('backend:contactmeimage')


def editcontactmeimagestatus(request, contactmeimage_id):
    counter = ContactMeImage.objects.filter(id=contactmeimage_id).first()
    if counter.status == "ACTIVE":

        ContactMeImage.objects.filter(id=counter.id).update(
            status="INACTIVE",
        )
        sweetify.success(request, 'Contact Me Image Status Updated Successfully')

    elif counter.status == "INACTIVE":
        ContactMeImage.objects.exclude(id=counter.id).update(
            status="INACTIVE",
        )
        ContactMeImage.objects.filter(id=counter.id).update(
            status="ACTIVE",
        )
        sweetify.error(request, 'Contact Me Image Status Updated Successfully')
    return redirect('backend:contactmeimage')


login_required()


def sendmessageimage(request):
    context = {
        'images': SendMessageImage.objects.all()
    }
    return render(request, 'PurpleAdmin-Free-Admin-Template/images/sendmessageimage.html', context)


def addsendmessageimage(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        workexpertForm = SendMessageImageForm(request.FILES, request.FILES)
        print(image)
        if workexpertForm.is_valid():
            SendMessageImage.objects.create(
                image=image,
            )
            sweetify.success(request, 'Send message Image/gif added Successfully')
        else:
            sweetify.error(request, 'Send message Image/gif not Added ')
    return redirect("backend:sendmessageimage")


def editsendmessageimage(request, sendmessageimage_id):
    counter = SendMessageImage.objects.filter(id=sendmessageimage_id).first()
    if request.method == 'POST':
        counterImageForm = SendMessageImageForm(request.POST, request.FILES, instance=counter)
        print(counterImageForm)
        if counterImageForm.is_valid():

            counterImageForm.save()
            sweetify.success(request, 'Send Message Image Updated Successfully')

        else:
            sweetify.error(request, 'Send Message Image not Updated ')
    return redirect("backend:sendmessageimage")


def deletesendmessageimage(request, sendmessageimage_id):
    counter = SendMessageImage.objects.filter(id=sendmessageimage_id).first()
    if counter:
        counter.image.delete()
        counter.delete()
        sweetify.success(request, 'Send Message Image/Gif Deleted Succesfully')
        return redirect("backend:sendmessageimage")

    else:
        sweetify.error(request, 'Error deleting Send Message Image/Gif')
        return redirect("backend:sendmessageimage")


def editsendmessageimagestatus(request, sendmessageimage_id):
    counter = SendMessageImage.objects.filter(id=sendmessageimage_id).first()
    if counter.status == "ACTIVE":

        SendMessageImage.objects.filter(id=counter.id).update(
            status="INACTIVE",
        )
        sweetify.success(request, ' Send Message Image/Gif Status Updated Successfully')

    elif counter.status == "INACTIVE":
        SendMessageImage.objects.exclude(id=counter.id).update(
            status="INACTIVE",
        )
        SendMessageImage.objects.filter(id=counter.id).update(
            status="ACTIVE",
        )
        sweetify.error(request, ' Send Message Image/Gif Status Updated Successfully')
    return redirect("backend:sendmessageimage")


login_required()


def workparticipation(request):
    contxt = {
        "wps": WorkParticipation.objects.all()
    }
    return render(request, "PurpleAdmin-Free-Admin-Template/workparticipation/workparticipation.html", contxt)


def addworkparticipation(request):
    if request.method == "POST":
        form = WorkParticipationForm(request.POST)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Work Participation Added Successfuly')
        else:
            sweetify.error(request, 'Error Adding Work Participation')
    return redirect("backend:workparticipation")


def editworkparticipation(request, work_pat_id):
    wp = WorkParticipation.objects.filter(id=work_pat_id).first()
    if request.method == "POST":
        form = WorkParticipationForm(request.POST, instance=wp)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Work Participation Updated Successfuly')
        else:
            sweetify.error(request, 'Error Updating Work Participation')
    return redirect("backend:workparticipation")


def deleteworkparticipation(request, work_pat_id):
    wp = WorkParticipation.objects.filter(id=work_pat_id).first()
    if wp:
        wp.delete()
        sweetify.success(request, 'Work Participation Deleted Successfuly')
    else:
        sweetify.error(request, "Error deleting work participation")
    return redirect("backend:workparticipation")


login_required()


def expertise(request):
    # print(Expertise.objects.all())
    contxt = {
        "exps": Expertise.objects.all(),
        "categories": Category.objects.all()
    }
    return render(request, "PurpleAdmin-Free-Admin-Template/Expertise/expertise.html", contxt)


def addexpertise(request):
    if request.method == "POST":
        form = ExpertiseForm(request.POST)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Expertise Added Successfuly')
        else:
            sweetify.error(request, 'Expertise Not Added')
    return redirect("backend:expertise")


def editexpertise(request, expertise_id):
    exp = Expertise.objects.filter(id=expertise_id).first()
    if request.method == "POST":
        form = ExpertiseForm(request.POST, instance=exp)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Expertise Added Successfuly')
        else:
            sweetify.error(request, 'Expertise Not Added')
    return redirect("backend:expertise")


def deleteexpertise(request, expertise_id):
    exp = Expertise.objects.filter(id=expertise_id).first()
    if exp:
        exp.delete()
        sweetify.success(request, 'Expertise Deleted Successfuly')
    else:
        sweetify.error(request, "Error deleting Expertise")
    return redirect("backend:expertise")


login_required()


def socialmedia(request):
    contxt = {
        "socials": SocialMedia.objects.all()
    }
    return render(request, "PurpleAdmin-Free-Admin-Template/socialmedia/socialmedia.html", contxt)


def addsocialmedia(request):
    if request.method == "POST":
        form = SocialForm(request.POST)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'SocialMedia Added Successfuly')
        else:
            sweetify.error(request, 'SocialMedia Not Added')
    return redirect("backend:socialmedia")


def editsocialmedia(request, social_id):
    exp = SocialMedia.objects.filter(id=social_id).first()
    if request.method == "POST":
        form = SocialForm(request.POST, instance=exp)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Social Media Added Successfuly')
        else:
            sweetify.error(request, 'Social Media Not Added')
    return redirect("backend:socialmedia")


def deletesocialmedia(request, social_id):
    exp = SocialMedia.objects.filter(id=social_id).first()
    if exp:
        exp.delete()
        sweetify.success(request, 'Social Media Deleted Successfuly')
    else:
        sweetify.error(request, "Error deleting Social Media")
    return redirect("backend:socialmedia")


login_required()


def portfolio(request):
    contxt = {
        "categories": Category.objects.all(),
        "portfolio": Portfolio.objects.all(),
    }
    return render(request, "PurpleAdmin-Free-Admin-Template/project/project.html", contxt)


def addportfolio(request):
    if request.method == "POST":
        form = PortfolioForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Portfolio Added Successfuly')
        else:
            sweetify.error(request, 'Portfolio Not Added')
    return redirect('backend:portfolio')


def editportfolio(request, portfolio_id):
    exp = Portfolio.objects.filter(id=portfolio_id).first()
    if request.method == "POST":
        form = PortfolioForm(request.POST, request.FILES, instance=exp)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Portfolio Added Successfuly')
        else:
            sweetify.error(request, 'Portfolio Not Added')
    return redirect('backend:portfolio')


def deleteportfolio(request, portfolio_id):
    exp = Portfolio.objects.filter(id=portfolio_id).first()
    if exp:
        exp.delete()
        sweetify.success(request, 'Portfolio Deleted Successfuly')
    else:
        sweetify.error(request, "Error deleting Portfolio")
    return redirect('backend:portfolio')


def editportfoliostatus(request, portfolio_id):
    counter = Portfolio.objects.filter(id=portfolio_id).first()
    if counter.status == "COOMINGSOON":

        Portfolio.objects.filter(id=counter.id).update(
            status="DONE",
        )
        sweetify.success(request, 'Project Status Updated Successfully')

    elif counter.status == "DONE":
        Portfolio.objects.filter(id=counter.id).update(
            status="COOMINGSOON",
        )
        sweetify.error(request, 'Project Status Updated Successfully')
    return redirect('backend:portfolio')


login_required()


def anouncementbar(request):
    contxt = {
        "announcements": AnnouncementBar.objects.all()
    }
    return render(request, "PurpleAdmin-Free-Admin-Template/announcementbar/announcementbar.html", contxt)


def addanouncementbar(request):
    if request.method == "POST":
        form = AnnouncementForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Announcement Added Successfuly')
        else:
            sweetify.error(request, 'Announcement Not Added')
    return redirect('backend:anouncementbar')


def editanouncementbar(request, announce_id):
    exp = AnnouncementBar.objects.filter(id=announce_id).first()
    if request.method == "POST":
        form = AnnouncementForm(request.POST, instance=exp)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Announcement Updeted Successfuly')
        else:
            sweetify.error(request, 'Announcement Not Updeted')
    return redirect('backend:anouncementbar')


def deleteanouncementbar(request, announce_id):
    exp = AnnouncementBar.objects.filter(id=announce_id).first()
    if exp:
        exp.delete()
        sweetify.success(request, 'Announcement Bar Deleted Successfuly')
    else:
        sweetify.error(request, "Error deleting Announcement Bar")
    return redirect('backend:anouncementbar')


def editanouncementbarstatus(request, announce_id):
    counter = AnnouncementBar.objects.filter(id=announce_id).first()
    if counter.status == "SHOW":

        AnnouncementBar.objects.filter(id=counter.id).update(
            status="HIDE",
        )
        sweetify.success(request, 'Announcement Bar Hidden')

    elif counter.status == "HIDE":
        AnnouncementBar.objects.exclude(id=counter.id).update(
            status="HIDE",
        )
        AnnouncementBar.objects.filter(id=counter.id).update(
            status="SHOW",
        )
        sweetify.success(request, 'Announcement Bar Shown')
    else:
        sweetify.success(request, 'Error Showing Announcement Bar ')
    return redirect('backend:anouncementbar')


def register(request):
    return render(request, "PurpleAdmin-Free-Admin-Template/pages/samples/register.html")


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST, request.FILES)
        print(form)
        if User.objects.count() == 0:
            if form.is_valid():
                form.save()
                sweetify.success(request, "User is successfuly registered", persistent='Continue', timer=3000)
                return redirect('backend:login')
            else:
                sweetify.error(request, "Error regestering user")
        else:
            sweetify.warning(request, 'There is a user already registered', persistent='Go Away')
    return redirect('backend:register')


def login(request):
    return render(request, "PurpleAdmin-Free-Admin-Template/pages/samples/login.html")


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        def adminemail(email):
            uz = User.objects.filter(Q(email__exact=email) | Q(username__exact=email)).first()
            if uz:
                return uz.username
            return None

        if User.objects.filter(Q(username__exact=username) | Q(email__exact=username)).first():
            user = authenticate(username=adminemail(username), password=password)
            if user is not None:
                if user.is_active:
                    if Admin.objects.filter(user_ptr_id=user.id).exists():
                        # login(request, user)
                        auth_login(request, user)
                        sweetify.success(request, 'Success', text='Welcome to Your Palace', persistent='Continue')
                        return redirect('backend:home')
                else:
                    sweetify.error(request, 'Error', text='Error',
                                   persistent='Retry')
                    return redirect('backend:login')
            else:
                sweetify.error(request, 'Error', text='Invalid login credentials', persistent='Retry')
                return redirect('backend:login')
    return redirect('backend:login')


def logout_user(request):
    logout(request)
    return redirect('backend:login')


def messages(request):
    names_list = []
    uzers = []
    names = ContactUs.objects.order_by("-created_at")

    for name in names:
        names_list.append(name.email)

    # users = []
    # for user in names_list:
    #     users.append(set(ContactUs.objects.filter(email=user).order_by("email")))

    context = {
        'messages': ContactUs.objects.all(),
        "names_list": set(names_list)
    }
    return render(request, "PurpleAdmin-Free-Admin-Template/chat/chat.html", context)


def sendemail(request):
    if request.method == 'POST':
        r_email = request.POST['receiver_email']
        subject = request.POST['subject']
        message = request.POST['message']

        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=EMAIL_HOST,
                recipient_list=[r_email, ],
                fail_silently=False,
            )
            ContactUs.objects.filter(email=r_email).update(
                status="READ",
            )
            sweetify.success(request, 'Success', text='Email Sent', persistent='Continue')
        except:
            print("errror")

    return redirect('backend:messages')


def deletemessages(request, email):
    contacts = ContactUs.objects.filter(email=email)
    if contacts:
        for contact in contacts:
            contact.delete()
    return redirect('backend:messages')


def account(request):
    contxt={
        'admins' : Admin.objects.all()
    }
    return render(request, "PurpleAdmin-Free-Admin-Template/Account/account.html",contxt)


def updateaccount(request, user_id):
    exp = Admin.objects.filter(id=user_id).first()
    if request.method == "POST":
        form = UpdateRegisterUserForm(request.POST, request.FILES, instance=exp)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'User Updeted Successfuly')
        else:
            sweetify.error(request, 'User Not Updeted')
    return redirect('backend:account')


def cv(request):
    contxt = {
        'educations': Education.objects.all().order_by('-start_d'),
        'experiences': Experience.objects.all().order_by('-start_d'),
        'software': Software.objects.all(),
        'language': Language.objects.all(),
    }
    return render(request, "PurpleAdmin-Free-Admin-Template/Cv/cv.html",contxt)


def addEducation(request):
    if request.method == "POST":
        form = EducationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Education Added Successfuly')
        else:
            sweetify.error(request, 'Education Not Added')
    return redirect('backend:cv')
def editEducation(request, edu_id):
    exp = Education.objects.filter(id=edu_id).first()
    if request.method == "POST":
        form = EducationForm(request.POST, instance=exp)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Education Updeted Successfuly')
        else:
            sweetify.error(request, 'Education Not Updeted')
    return redirect('backend:cv')
def deleteEducation(request, edu_id):
    contact = Education.objects.filter(id=edu_id).first()
    if contact:
       contact.delete()
       sweetify.success(request, 'Education History Deleted Successfuly')
    else:
       sweetify.error(request, "Error deleting Education History")

    return redirect('backend:cv')


def addExperience(request):
    if request.method == "POST":
        form = CvExperienceForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Experience Added Successfuly')
        else:
            sweetify.error(request, 'Experience Not Added')
    return redirect('backend:cv')
def editExperience(request, exp_id):
    exp = Experience.objects.filter(id=exp_id).first()
    if request.method == "POST":
        form = EducationForm(request.POST, instance=exp)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Experience Updeted Successfuly')
        else:
            sweetify.error(request, 'Experience Not Updeted')
    return redirect('backend:cv')
def deleteExperience(request, exp_id):
    contact = Experience.objects.filter(id=exp_id).first()
    if contact:
       contact.delete()
       sweetify.success(request, 'Experience Deleted Successfully')
    else:
       sweetify.error(request, "Error deleting Experience")

    return redirect('backend:cv')



def addSoftware(request):
    if request.method == "POST":
        form = CvSoftwareForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Software Added Successfuly')
        else:
            sweetify.error(request, 'Software Not Added')
    return redirect('backend:cv')
def editSoftware(request, software_id):
    exp = Software.objects.filter(id=software_id).first()
    if request.method == "POST":
        form = CvSoftwareForm(request.POST, instance=exp)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Software Updeted Successfuly')
        else:
            sweetify.error(request, 'Software Not Updeted')
    return redirect('backend:cv')
def deleteSoftware(request, software_id):
    contact =Software.objects.filter(id=software_id).first()
    if contact:
       contact.delete()
       sweetify.success(request, 'Software Deleted Successfully')
    else:
       sweetify.error(request, "Error deleting Software")

    return redirect('backend:cv')


def addLanguage(request):
    if request.method == "POST":
        form = CvLanguageForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Language Added Successfuly')
        else:
            sweetify.error(request, 'Language Not Added')
    return redirect('backend:cv')

def editLanguage(request, language_id):
    exp =  Language.objects.filter(id=language_id).first()
    if request.method == "POST":
        form = CvLanguageForm(request.POST, instance=exp)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Language Updeted Successfuly')
        else:
            sweetify.error(request, 'Language Not Updeted')
    return redirect('backend:cv')

def deleteLanguage(request, language_id):
    contact = Language.objects.filter(id=language_id).first()
    if contact:
       contact.delete()
       sweetify.success(request, 'Language Deleted Successfully')
    else:
       sweetify.error(request, "Error deleting Language")

    return redirect('backend:cv')
























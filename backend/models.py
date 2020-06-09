from datetime import date

from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.utils import timezone


class Carousel(models.Model):
    image = models.ImageField(max_length=200, null=False, blank=False, upload_to="carousel")
    title = models.CharField(max_length=200, null=False, blank=False)
    sub_title = models.CharField(max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.title)


class About(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    image = models.ImageField(max_length=200, null=False, blank=False, upload_to="About")
    description = models.TextField()
    email = models.CharField(max_length=200, null=False, blank=False)
    phone = models.CharField(max_length=200, null=False, blank=False)
    location_url = models.CharField(max_length=20000, null=True, blank=True)
    address = models.CharField(max_length=200, null=False, blank=False)
    signature = models.ImageField(max_length=200, null=False, blank=False, upload_to="signature")
    date_of_birth = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return '%s' % (self.email)

    @property
    def age(self):
        today = date.today()
        return today.year - self.date_of_birth.year - (
                    (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))


class Hobbies(models.Model):
    icon = models.CharField(max_length=200, null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.name)


class Speciality(models.Model):
    icon = models.CharField(max_length=200, null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.name)


class WorkParticipation(models.Model):
    start_end_dates = models.CharField(max_length=200, null=False, blank=False)
    title = models.CharField(max_length=200, null=False, blank=False)
    position = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.title)


class Category(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.name)


class Expertise(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    language = models.CharField(max_length=200, null=False, blank=False)
    percentage = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.language)


class Progresscounter(models.Model):
    happy_clients = models.CharField(max_length=200, null=False, blank=False)
    cups_of_coffee = models.CharField(max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.happy_clients)


class Portfolio(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    image = models.ImageField(max_length=200, null=False, blank=False, upload_to="project")
    name = models.CharField(max_length=200, null=False, blank=False)
    link = models.CharField(max_length=200, null=True, blank=True)
    CHOICES = {
        ('COOMINGSOON', 'Coomingsoon'),
        ('DONE', 'Done'),
    }
    status = models.CharField(max_length=200, null=True, blank=True, choices=CHOICES, default='DONE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.name)


class ContactUs(models.Model):
    first_name = models.CharField(max_length=300, null=False, blank=False)
    last_name = models.CharField(max_length=300, null=False, blank=False)
    email = models.CharField(max_length=300, null=False, blank=False)
    subject = models.CharField(max_length=300, null=True, blank=True)
    message = models.TextField()
    CHOICES = {
        ('READ', 'Read'),
        ('UNREAD', 'Unread'),
        ('TRASH', 'Trash'),
    }
    status = models.CharField(max_length=200, null=True, blank=True, choices=CHOICES, default='UNREAD')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

        # def users(self):
        #     uzer = []
        #     users = ContactUs.objects.all()
        #     for email in users:
        #         uzer.append(email.email)
        #
        #     return list(set(uzer))
        # def names(self):
        #     names_list=[]
        #     names = ContactUs.objects.all()
        #     for name in names:
        #         names_list.append(name.first_name +" "+ name.last_name)

        return list(set(names_list))


class Newsletter(models.Model):
    email = models.CharField(max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.email)


class SocialMedia(models.Model):
    icon = models.CharField(max_length=200, null=False, blank=False)
    social_name = models.CharField(max_length=300, null=False, blank=False)
    social_url = models.URLField(max_length=300, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.social_name, self.social_url)


class CounterImages(models.Model):
    image = models.ImageField(max_length=200, null=False, blank=False, upload_to="counterimages")
    CHOICES = {
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
    }
    status = models.CharField(max_length=200, null=True, blank=True, choices=CHOICES, default='INACTIVE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.status)


class WorkExpertise(models.Model):
    image = models.ImageField(max_length=200, null=False, blank=False, upload_to="workexpertimages")
    CHOICES = {
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
    }
    status = models.CharField(max_length=200, null=True, blank=True, choices=CHOICES, default='INACTIVE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.status)


class AvailableForTheProject(models.Model):
    image = models.ImageField(max_length=200, null=False, blank=False, upload_to="availablefortheproject")
    CHOICES = {
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
    }
    status = models.CharField(max_length=200, null=True, blank=True, choices=CHOICES, default='INACTIVE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.status)


class ContactMeImage(models.Model):
    image = models.ImageField(max_length=200, null=False, blank=False, upload_to="contactme")
    CHOICES = {
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
    }
    status = models.CharField(max_length=200, null=True, blank=True, choices=CHOICES, default='INACTIVE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.status)


class SendMessageImage(models.Model):
    image = models.ImageField(max_length=200, null=False, blank=False, upload_to="sendmessageimage")
    CHOICES = {
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
    }
    status = models.CharField(max_length=200, null=True, blank=True, choices=CHOICES, default='INACTIVE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.status)


class Admin(get_user_model()):
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    birth_day = models.DateTimeField(default=timezone.now())
    admin_profile = models.ImageField(upload_to='admin_images', max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class AnnouncementBar(models.Model):
    backgroud_color = models.CharField(max_length=200, null=False, blank=False)
    text_color = models.CharField(max_length=200, null=False, blank=False)
    message = models.CharField(max_length=200, null=False, blank=False)
    icon = models.CharField(max_length=200, null=True, blank=True)
    CHOICESX = {
        ('SHOW', 'Show'),
        ('HIDE', 'Hide'),
    }
    status = models.CharField(max_length=200, null=True, blank=True, choices=CHOICESX, default='HIDE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s  %s' % (self.message, self.status)


# class MyCv(models.Model):
#     objective = models.TextField()

class Education(models.Model):
    start_d = models.DateTimeField(default=timezone.now())
    end_d = models.DateTimeField(default=timezone.now())
    school = models.CharField(max_length=200, null=False, blank=False)
    position = models.CharField(max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s  %s' % (self.school, self.position)


class Experience(models.Model):
    start_d = models.DateTimeField(default=timezone.now())
    end_d = models.DateTimeField(default=timezone.now())
    institution = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField()
    position = models.CharField(max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s  %s' % (self.institution, self.position)


class Software(models.Model):
    software = models.CharField(max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.software)


class Language(models.Model):
    language = models.CharField(max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.language)

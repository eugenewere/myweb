from django import forms
from django.contrib.auth.forms import UserCreationForm

from backend.models import *


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name',]

class CarouselImageForm(forms.ModelForm):

    class Meta:
        model = Carousel
        fields = ['image','title','sub_title',]

class AboutMeForm(forms.ModelForm):

    class Meta:
        model = About
        fields = ['image','name','phone','email','signature','address', 'date_of_birth', 'description','location_url']


class HobbiesForm(forms.ModelForm):

    class Meta:
        model = Hobbies
        fields = ['name','icon',]


class ServicesForm(forms.ModelForm):

    class Meta:
        model = Speciality
        fields = ['name','icon','description',]


class ProgressForm(forms.ModelForm):

    class Meta:
        model = Progresscounter
        fields = ["cups_of_coffee","happy_clients"]


class CounterImageForm(forms.ModelForm):

    class Meta:
        model = CounterImages
        fields = ['image',]

class WorkExpImageForm(forms.ModelForm):

    class Meta:
        model = WorkExpertise
        fields = ['image',]


class AvailableForTheProjectImageForm(forms.ModelForm):

    class Meta:
        model = AvailableForTheProject
        fields = ['image',]


class ContactMeImageForm(forms.ModelForm):

    class Meta:
        model = ContactMeImage
        fields = ['image',]

class SendMessageImageForm(forms.ModelForm):

    class Meta:
        model = SendMessageImage
        fields = ['image',]

class WorkParticipationForm(forms.ModelForm):

    class Meta:
        model = WorkParticipation
        fields = ['start_end_dates','title','position','description']

class ExpertiseForm(forms.ModelForm):

    class Meta:
        model = Expertise
        fields = ['language','percentage','category',]


class SocialForm(forms.ModelForm):

    class Meta:
        model = SocialMedia
        fields = ['social_name','social_url','icon',]


class PortfolioForm(forms.ModelForm):

    class Meta:
        model = Portfolio
        fields = ['image', 'link', 'name', 'category']



class AnnouncementForm(forms.ModelForm):

    class Meta:
        model = AnnouncementBar
        fields = ['backgroud_color', 'text_color', 'message', 'icon']




class MessageForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = ['first_name', 'last_name', 'email', 'subject', 'message', ]


class NewsLetterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = ['email' ]


class RegisterUserForm(UserCreationForm):

    class Meta:
        model = Admin
        fields = ['password1','password2','email','username','first_name','last_name', 'phone_number','birth_day','admin_profile']


class UpdateRegisterUserForm(forms.ModelForm):

    class Meta:
        model = Admin
        fields = ['email','username','first_name','last_name', 'phone_number','birth_day','admin_profile', ]


class EducationForm(forms.ModelForm):

    class Meta:
        model = Education
        fields = ['start_d','end_d','school','position' ]


class CvExperienceForm(forms.ModelForm):

    class Meta:
        model = Experience
        fields = ['start_d', 'end_d', 'institution', 'position', 'description', ]


class CvSoftwareForm(forms.ModelForm):

    class Meta:
        model = Software
        fields = ['software', ]


class CvLanguageForm(forms.ModelForm):

    class Meta:
        model = Language
        fields = ['language', ]




































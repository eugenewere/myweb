
from django.urls import path
from . import views

app_name = 'backend'
urlpatterns = [
    path('', views.home,  name='home'),
    path('category/', views.category,  name='category'),
    path('addcategory/', views.addcategory,  name='addcategory'),
    path('deletecategory/<int:category_id>/', views.deletecategory,  name='deletecategory'),
    path('editcategory/<int:category_id>/', views.editcategory,  name='editcategory'),

    path('register/', views.register, name='register'),
    path('register_user/', views.register_user, name='register_user'),
    path('login/', views.login, name='login'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout'),


    # carousell
    path('carousel/', views.view_carousel, name='view_carousel'),
    path('addcarousel/', views.addcarousel, name='addcarousel'),
    path('carousel/delete/<int:carousel_id>', views.carousel_delete, name='carousel-delete'),
    path('carousel/edit/<int:carousel_id>', views.carousel_edit, name='carousel-edit'),


    path('about_me', views.about_me, name='about_me'),
    path('addabout_me', views.addabout_me, name='addabout_me'),
    path('editabout_me/<int:about_id>', views.editabout_me, name='editabout_me'),
    path('deleteabout_me/<int:about_id>', views.deleteabout_me, name='deleteabout_me'),


    path('hobbies/', views.hobbies, name='hobbies'),
    path('addhobbies/', views.addhobbies, name='addhobbies'),
    path('edithobbies/<int:hobby_id>', views.edithobbies, name='edithobbies'),
    path('deletehobbies/<int:hobby_id>', views.deletehobbies, name='deletehobbies'),


    path('services/', views.services, name='services'),
    path('addservices/', views.addservices, name='addservices'),
    path('editservices/<int:service_id>', views.editservices, name='editservices'),
    path('deleteservices/<int:service_id>', views.deleteservices, name='deleteservices'),

    path('progresscounter/', views.progresscounter, name='progresscounter'),
    path('addprogresscounter/', views.addprogresscounter, name='addprogresscounter'),
    path('editprogresscounter/<int:pc_id>', views.editprogresscounter, name='editprogresscounter'),
    path('deleteprogresscounter/<int:pc_id>', views.deleteprogresscounter, name='deleteprogresscounter'),



    path('counterimages/', views.counterimages, name='counterimages'),
    path('addcounterimages/', views.addcounterimages, name='addcounterimages'),
    path('editcounterimages/<int:counter_image_id>', views.editcounterimages, name='editcounterimages'),
    path('deletecounterimages/<int:counter_image_id>', views.deletecounterimages, name='deletecounterimages'),
    path('editcounterimagesstatus/<int:counter_image_id>', views.editcounterimagesstatus, name='editcounterimagesstatus'),



    path('workexpertimage/', views.workexpertimage, name='workexpertimage'),
    path('addworkexpertimage/', views.addworkexpertimage, name='addworkexpertimage'),
    path('editworkexpertimage/<int:workexpertimage_id>', views.editworkexpertimage, name='editworkexpertimage'),
    path('deleteworkexpertimage/<int:workexpertimage_id>', views.deleteworkexpertimage, name='deleteworkexpertimage'),
    path('editworkexpertimagestatus/<int:workexpertimage_id>', views.editworkexpertimagestatus, name='editworkexpertimagestatus'),



    path('availforprojimage/', views.availforprojimage, name='availforprojimage'),
    path('addavailforprojimage/', views.addavailforprojimage, name='addavailforprojimage'),
    path('editavailforprojimage/<int:availforprojimage_id>', views.editavailforprojimage, name='editavailforprojimage'),
    path('deleteavailforprojimage/<int:availforprojimage_id>', views.deleteavailforprojimage, name='deleteavailforprojimage'),
    path('editavailforprojimagestatus/<int:availforprojimage_id>', views.editavailforprojimagestatus, name='editavailforprojimagestatus'),



    path('contactmeimage/', views.contactmeimage, name='contactmeimage'),
    path('addcontactmeimage/', views.addcontactmeimage, name='addcontactmeimage'),
    path('editcontactmeimage/<int:contactmeimage_id>', views.editcontactmeimage, name='editcontactmeimage'),
    path('deletecontactmeimage/<int:contactmeimage_id>', views.deletecontactmeimage, name='deletecontactmeimage'),
    path('editcontactmeimagestatus/<int:contactmeimage_id>', views.editcontactmeimagestatus, name='editcontactmeimagestatus'),


    path('sendmessageimage/', views.sendmessageimage, name='sendmessageimage'),
    path('addsendmessageimage/', views.addsendmessageimage, name='addsendmessageimage'),
    path('editsendmessageimage/<int:sendmessageimage_id>', views.editsendmessageimage, name='editsendmessageimage'),
    path('deletesendmessageimage/<int:sendmessageimage_id>', views.deletesendmessageimage, name='deletesendmessageimage'),
    path('editsendmessageimagestatus/<int:sendmessageimage_id>', views.editsendmessageimagestatus, name='editsendmessageimagestatus'),


    path('workparticipation/', views.workparticipation, name='workparticipation'),
    path('addworkparticipation/', views.addworkparticipation, name='addworkparticipation'),
    path('editworkparticipation/<int:work_pat_id>', views.editworkparticipation, name='editworkparticipation'),
    path('deleteworkparticipation/<int:work_pat_id>', views.deleteworkparticipation, name='deleteworkparticipation'),

    path('expertise/', views.expertise, name='expertise'),
    path('addexpertise/', views.addexpertise, name='addexpertise'),
    path('editexpertise/<int:expertise_id>', views.editexpertise, name='editexpertise'),
    path('deleteexpertise/<int:expertise_id>', views.deleteexpertise, name='deleteexpertise'),

    path('socialmedia/', views.socialmedia, name='socialmedia'),
    path('addsocialmedia/', views.addsocialmedia, name='addsocialmedia'),
    path('editsocialmedia/<int:social_id>', views.editsocialmedia, name='editsocialmedia'),
    path('deletesocialmedia/<int:social_id>', views.deletesocialmedia, name='deletesocialmedia'),

    path('portfolio/', views.portfolio, name='portfolio'),
    path('addportfolio/', views.addportfolio, name='addportfolio'),
    path('editportfolio/<int:portfolio_id>', views.editportfolio, name='editportfolio'),
    path('deleteportfolio/<int:portfolio_id>', views.deleteportfolio, name='deleteportfolio'),
    path('editportfoliostatus/<int:portfolio_id>', views.editportfoliostatus, name='editportfoliostatus'),

    path('anouncementbar/', views.anouncementbar, name='anouncementbar'),
    path('addanouncementbar/', views.addanouncementbar, name='addanouncementbar'),
    path('editanouncementbar/<int:announce_id>', views.editanouncementbar, name='editanouncementbar'),
    path('editanouncementbarstatus/<int:announce_id>', views.editanouncementbarstatus, name='editanouncementbarstatus'),
    path('deleteanouncementbar/<int:announce_id>', views.deleteanouncementbar, name='deleteanouncementbar'),



    path('messages/', views.messages, name='messages'),
    path('deletemessages/<str:email>', views.deletemessages, name='deletemessages'),
    path('sendemail/', views.sendemail, name='sendemail'),

    path('account/', views.account, name='account'),
    path('updateaccount/<int:user_id>', views.updateaccount, name='updateaccount'),

    path('cv/', views.cv, name='cv'),

    path('addEducation/', views.addEducation, name='addEducation'),
    path('editEducation/<int:edu_id>', views.editEducation, name='editEducation'),
    path('deleteEducation/<int:edu_id>', views.deleteEducation, name='deleteEducation'),

    path('addExperience/', views.addExperience, name='addExperience'),
    path('editExperience/<int:exp_id>', views.editExperience, name='editExperience'),
    path('deleteExperience/<int:exp_id>', views.deleteExperience, name='deleteExperience'),

    path('addSoftware/', views.addSoftware, name='addSoftware'),
    path('editSoftware/<int:software_id>', views.editSoftware, name='editSoftware'),
    path('deleteSoftware/<int:software_id>', views.deleteSoftware, name='deleteSoftware'),

    path('addLanguage/', views.addLanguage, name='addLanguage'),
    path('editLanguage/<int:language_id>', views.editLanguage, name='editLanguage'),
    path('deleteLanguage/<int:language_id>', views.deleteLanguage, name='deleteLanguage'),




]





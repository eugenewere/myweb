from django.urls import path
from . import views

app_name = 'frontend'
urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('addmessage/', views.addmessage, name='addmessage'),
    path('addsubscribers/', views.addsubscribers, name='addsubscribers'),
    path('view_cv/', views.view_cv, name='view_cv'),

]
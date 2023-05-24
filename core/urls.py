from cgitb import handler
from django.urls import path, include
from . import views

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),

    path('', views.home),
    path('aboutus/', views.aboutus),
    path('whatwedo/', views.whatwedo),
    path('contact_us/', views.contact),
    path('alumnis/', views.alumnis)
]


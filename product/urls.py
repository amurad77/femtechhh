from django.urls import path, include
from . import views

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    # path('alumnis/<slug:slug>/', views.alumnis, name='alumnis'),

    path('programs/', views.programs),
    path('programs-details/<slug:slug>/', views.programs_details, name='programs_details'),
    path('upcoming-programs/', views.upcoming_programs),
    path('complete-programs/', views.complete_programs),

    path('events/', views.events),
    path('event-details/<slug:slug>/', views.event_details, name='event_details'),
    path('upcoming-events/', views.upcoming_events),
    path('complete-events/', views.complete_events),
    
    path('news/', views.news),
    path('news-detail/<slug:slug>/', views.news_details, name='news_details')
]
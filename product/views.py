import imp
from multiprocessing import context
from operator import imod
from django.shortcuts import render
# from core.models import Program, Alumnis
from .models import Event, News, Programs
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
# from core.models import Program

# Create your views here.
# def alumnis(request, slug):
#     program = get_object_or_404(Program, slug = slug)
#     alumnis = Alumnis.objects.filter(program = program)

#     context = {
#         'alumnis' : alumnis,
#         'program' : program,
#     }

#     return render(request, 'single-alumnis.html', context)


def programs(request):
    upcoming = Programs.objects.filter(is_published = True).order_by('-id')[0:][:3]
    complete = Programs.objects.filter(is_published = False).order_by('-id')[0:][:3]

    context = {
        'upcoming' : upcoming,
        # 'page_obj': page_obj,
        'complete' : complete,
    }
    return render(request, 'programs.html', context)

def upcoming_programs(request):
    upcoming = Programs.objects.filter(is_published = True).order_by('-id')

    page_num = request.GET.get('page', 1)

    paginator = Paginator(upcoming, 12) # 6 employees per page

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'upcoming' : page_obj.object_list,
        'page_obj': page_obj,
    }
    return render(request, 'upcoming-programs.html', context)

def complete_programs(request):
    complete = Programs.objects.filter(is_published = False).order_by('-id')

    page_num = request.GET.get('page', 1)

    paginator = Paginator(complete, 12) # 6 employees per page

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'complete' : page_obj.object_list,
        'page_obj': page_obj,
    }
    return render(request, 'complete-programs.html', context)

def programs_details(request, slug):
    program = get_object_or_404(Programs, slug = slug)
    context = {
        'program' : program,
    }
    return render(request, 'program-details.html', context)



def events(request):
    complete = Event.objects.filter(is_published = False).order_by('-id')[0:][:3]

    upcoming = Event.objects.filter(is_published = True).order_by('-id')[0:][:3]


    context = {
        'upcoming' : upcoming,
        # 'page_obj': page_obj,
        'complete' : complete,
    }
    return render(request, 'events.html', context)

def upcoming_events(request):
    upcoming = Event.objects.filter(is_published = True).order_by('-id')

    page_num = request.GET.get('page', 1)

    paginator = Paginator(upcoming, 12) # 6 employees per page

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'upcoming' : page_obj.object_list,
        'page_obj': page_obj,
    }
    return render(request, 'upcoming-events.html', context)

def complete_events(request):
    complete = Event.objects.filter(is_published = False).order_by('-id')

    page_num = request.GET.get('page', 1)

    paginator = Paginator(complete, 12) # 6 employees per page

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'complete' : page_obj.object_list,
        'page_obj': page_obj,
    }
    return render(request, 'complete-events.html', context)

def event_details(request, slug):
    event = get_object_or_404(Event, slug = slug)
    

    context = {

        'event' : event,
    }
    # print(event.other_image1)
    return render(request, 'event-details.html', context)



def news(request):
    news = News.objects.all().order_by('-id')

    page_num = request.GET.get('page', 1)

    paginator = Paginator(news, 12) # 6 employees per page

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'news' : page_obj.object_list,
        'page_obj': page_obj,
    }

    return render(request, 'news.html', context)

def news_details(request, slug):
    news = get_object_or_404(News, slug = slug)

    context = {
        'news' : news
    }

    return render(request, 'newsdetail.html', context)
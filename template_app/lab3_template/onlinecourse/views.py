from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import Course, Lesson, Enrollment
from django.urls import reverse
from django.views import generic
from django.http import Http404

# Create your views here.


def popular_course_list(request):
    context = {}
    # if request is GET
    if request.method == 'GET':
        course_list = Course.objects.order_by('-total_enrollment')[:10]
        context['course_list'] = course_list
        return render(request, 'onlinecourse/course_list.html', context)


def enroll(request, course_id):
    if request.method == 'POST':
        course = get_object_or_404(Course, pk=course_id)
        course.total_enrollment += 1
        course.save()

        return HttpResponseRedirect(reverse(viewname='onlinecourse:course_details', args=(course_id,)))


def course_details(request, course_id):
    context = {}
    if request.method == 'GET':
        try:
            course = Course.objects.get(pk=course_id)
            context['course'] = course
            return render(request=request, template_name='onlinecourse/course_detail.html', context=context)
        except Course.DoesNotExist:
            raise Http404("No courses matches the given id.")

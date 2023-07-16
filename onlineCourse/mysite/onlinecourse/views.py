from django.shortcuts import render
from django.http import HttpResponse
from .models import Course

# Create your views here.


def course_list(request):
    course = Course.objects.get(pk=1)
    template = "<html>" \
        "<body>The first course we get is `%s.`" \
        "</body>" \
        "</html>" % course.name
    return HttpResponse(content=template)

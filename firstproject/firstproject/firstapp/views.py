from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

# Create your views here.


def index(request):
    # Create sinple html page as string
    template = "<html>" \
        "This is your first view" \
        "</html>"

    # Return the template as content argument in HHTP response
    return HttpResponse(content=template)


def get_date(request):
    today = date.today()

    template = "<html>" \
        f"Today's date is {today}" \
        "</html>"

    return HttpResponse(content=template)

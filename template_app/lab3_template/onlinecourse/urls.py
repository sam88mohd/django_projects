from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'onlinecourse'
urlpatterns = [
    # Add path here
    path(route='', view=views.popular_course_list, name='popular_course_list'),
    path(route='course/<int:course_id>/enroll/',
         view=views.enroll, name='enroll'),
    path(route='course/<int:course_id>/',
         view=views.course_details, name='course_details')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

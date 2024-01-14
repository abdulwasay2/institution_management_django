from django.urls import path

from . import views


urlpatterns = [
    path('public_courses/', views.CoursePublicView.as_view(), name='public-courses'),
]
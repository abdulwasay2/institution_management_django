from django.urls import path, include
# from rest_framework import routers

from . import views


# router = routers.DefaultRouter()
# router.register(r'roll_number_slip', views.StudentRollNumberSlipView, basename='roll-number-slip')

urlpatterns = [
    path('student/roll_number_slip/', views.StudentRollNumberSlipView.as_view(), name='roll-number-slip'),
]
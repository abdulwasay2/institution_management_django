from django.views.generic.base import TemplateView
 

class Login(TemplateView):
    template_name = 'registeration/login.html'


class About(TemplateView):
    template_name = 'about.html'


class Home(TemplateView):
    template_name = 'home.html'


class RollNumberSlips(TemplateView):
    template_name = 'students/roll_number_slips.html'
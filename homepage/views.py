from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from .models import user

def homepage(request):
    currentUser = user.objects.get(id=1)
    template = loader.get_template('homepage/practicePage.html')
    context = {
        'full_name' : currentUser.fullName,
        'city' : currentUser.city,
        'orientation' : currentUser.orientation,
        'last_online' : currentUser.lastOnline,
        'interests' : currentUser.interests,
        'about_me' : currentUser.aboutMe,
    }
    return HttpResponse(template.render(context, request))
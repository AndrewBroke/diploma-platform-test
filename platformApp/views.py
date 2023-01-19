from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import *
import random

# Create your views here.
def index(request):
    context = {
        "title": "Platform"
    }
    return render(request, "platform/index.html", context)



def test_view(request, theme_id):
    questions_privacy_all = SimpleQuestion.objects.filter(corrent_answer=2)
    questions_privacy_send = []
    i = random.randint(0, len(questions_privacy_all) - 1)
    
    context = {
        "title": "Test на тему 1"
    }
    return render(request, f"platform/tests/test-theme-{theme_id}.html", context)
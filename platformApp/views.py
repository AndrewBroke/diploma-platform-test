from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    context = {
        "title": "Platform"
    }
    return render(request, "platform/index.html", context)

def test_view(request, theme_id):
    context = {
        "title": "Test на тему 1"
    }
    return render(request, f"platform/tests/test-theme-{theme_id}.html", context)
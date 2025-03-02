# RiffMates/home/views.py
from django.http import HttpResponse
from django.shortcuts import render
from .models import Carousel, Post



def credits(request):
    content = "Nicky\nYour Name"
    return HttpResponse(content, content_type="text/plain")

def post_list(request):
    posts = Post.objects.all()
    carousels = Carousel.objects.filter(active=True)
    return render(request, 'home/post_list.html', {'posts': posts, 'carousels': carousels})


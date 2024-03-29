from django.shortcuts import render
from places.models import Comment
from datetime import datetime

def index(request):
    comments = Comment.objects.all().order_by('-created_at')
    days = {}
    for comment in comments:
        days[comment.id] = (datetime.now() - datetime.combine(comment.created_at, datetime.min.time())).days
    return render(request, 'landing.html', {"comments": comments, 'days':days})
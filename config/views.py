from django.shortcuts import render
from places.models import Comment
from datetime import datetime
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    comments = Comment.objects.exclude(user=request.user).order_by('-created_at')
    days = {}
    for comment in comments:
        days[comment.id] = (datetime.now() - datetime.combine(comment.created_at, datetime.min.time())).days
    return render(request, 'landing.html', {"comments": comments, 'days':days})
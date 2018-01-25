from django.shortcuts import render
from .models import Photo
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def post_list(request):
    posts = Photo.objects.all()
    return render(request, 'photo/list.html', {'posts':posts})
#posts 라는 이름으로 Photo 에 있는 모든 것을 옮김.


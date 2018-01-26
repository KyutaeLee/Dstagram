from django.shortcuts import render, redirect
from .models import Photo
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy

# Create your views here.

@login_required
def post_list(request):
    posts = Photo.objects.all()
    return render(request, 'photo/list.html', {'posts':posts})
#posts 라는 이름으로 Photo 에 있는 모든 것을 옮김.

class UploadView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/upload.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id

        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form':form})

class PhotoDeleteV(LoginRequiredMixin, DeleteView):
    model = Photo
    success_url = reverse_lazy('post_list')


from django.shortcuts import render
from django.views.generic import (ListView, CreateView, DeleteView, UpdateView, TemplateView)
from ejemplo_dos.models import Post

def index(request):
    return render(request, "ejemplo_dos/index.html"),


class PostList(TemplateView):
    template_name = 'ejemplo_dos/post_list.html'


class PostCrear(CreateView):
    model = Post
    success_url = "ejemplo-dos/listar"
    fields = '__all__'



# Create your views here.

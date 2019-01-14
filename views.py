from django.shortcuts import render
from .forms import ImgForm
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy
 
from .models import ImageFiles
from img.lib import img_predict
import os

# Create your views here.

class ImgDetailView(DetailView):
    model = ImageFiles

class ImgUpdateView(UpdateView):
    model = ImageFiles
    form_class = ImgForm
    template_name = "img/imagefiles_update_form.html"
    
    def get_success_url(self):
        model_pk = self.kwargs['pk']
        url = reverse_lazy("detail", kwargs={"pk": model_pk})
        return url

class ImgListView(ListView):
    model = ImageFiles
    paginate_by = 10
 
class ImgCreateView(CreateView):
    model = ImageFiles
    form_class = ImgForm
    success_url = reverse_lazy("index")


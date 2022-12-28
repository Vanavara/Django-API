from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth.decorators import login_required

# from .forms import PeakForm
from rest_framework import viewsets
from .models import Peak
from .serializers import PeakSerializer


class PeakView(viewsets.ModelViewSet):
    queryset = Peak.objects.all()
    serializer_class = PeakSerializer


# # Добавлено 28.12
# class HomePageView(ListView):
#     model = Peak
#     template_name = 'index.html'
#
# # class CreatPostView(CreateView):
# #     model = CreatPostView
# #     form_class = PostForm
# #     template_name = 'post.html'
# #     success_url = reverse_lazy('index')
=======
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth.decorators import login_required

# from .forms import PeakForm
from rest_framework import viewsets
from .models import Peak
from .serializers import PeakSerializer


class PeakView(viewsets.ModelViewSet):
    queryset = Peak.objects.all()
    serializer_class = PeakSerializer


# # Добавлено 28.12
# class HomePageView(ListView):
#     model = Peak
#     template_name = 'index.html'
#
# # class CreatPostView(CreateView):
# #     model = CreatPostView
# #     form_class = PostForm
# #     template_name = 'post.html'
# #     success_url = reverse_lazy('index')

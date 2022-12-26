from django.shortcuts import render
from rest_framework import viewsets
from .models import Peak
from .serializers import PeakSerializer


class PeakView(viewsets.ModelViewSet):
    queryset = Peak.objects.all()
    serializer_class = PeakSerializer
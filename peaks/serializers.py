from rest_framework import serializers
from .models import Peak


class PeakSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Peak
        fields = ('id', 'peak_name', 'url', 'peak_coordinates', 'peak_height', 'user_name', 'phone', 'email_address', 'peak_image')


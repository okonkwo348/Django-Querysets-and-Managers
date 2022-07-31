from rest_framework import serializers
from . models import Link

class Linkserializer(serializers.Modelserializer):
    class Meta:

         model = Link
         fields = '_all_'
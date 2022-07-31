from django.shortcuts import render
from . models import Link
from . serializers import LinkSerializer
from rest_framework import ListApis
from rest_framework import CreateApis
from rest_framework import DetailApis
from rest_framework import UpdateApis
from rest_framework import DeleteApis

class LinkListApi(ListApis.ModelListApi):
      queryset = Link.objects.filter(active=True)
      serializer_class = LinkSerializer

class LinkCreateApi(CreateApis.ModelCreateApi):
      queryset = Link.objects.filter(active=True)
      serializer_class = LinkSerializer

class LinkDetailApi(DetailApis.ModelDetailApi):
      queryset = Link.objects.filter(active=True)
      serializer_class = LinkSerializer

class LinkUpdateApi(UpdateApis.ModelUpdateApi):
      queryset = Link.object.filter(active=True)
      serializer_class = LinkSerializer

class LinkDeleteApi(DeleteApis.ModelDeleteAp):
      queryset= Link.objects.filter(active=True)
      serializer_class = LinkSerializer
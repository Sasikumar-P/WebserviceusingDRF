# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from quickstart.models import Book
from quickstart.serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
	 queryset = Book.objects.all()
	 serializer_class = BookSerializer
	
# Create your views here.

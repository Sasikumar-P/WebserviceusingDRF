
from rest_framework import serializers
from quickstart.models import Book

class BookSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Book
		fields = ('title', 'name')
	

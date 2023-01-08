from rest_framework import serializers

from .models import Book, User


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title', 'description', 'author', 'genre', 'buyed_at', 'normal_price', 'buy_place', 'payed', 'is_read', 'rating', 'notice']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'password', 'email']


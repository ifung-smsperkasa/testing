from .models import Category
from .models import Perizinan
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username')

class PerizinanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Perizinan
        fields = ('id','employee','start','end','category','reason')

class CategorySerializer(serializers.ModelSerializer):
    perizinan = PerizinanSerializer(many=True,read_only=True)
    class Meta:
        model = Category
        fields = ('name','note','perizinan')

class CustomSerializer(serializers.RelatedField):
    def to_representation(self, value):
        """
        Serialize tagged objects to a simple textual representation.
        """
        if isinstance(value, Perizinan):
            serialize= Perizinan(value)
        elif isinstance(value, User):
            serialize =  UserSerializer(value)
        else:
            raise Exception('Unexpected type of tagged object')
        return serialize.data

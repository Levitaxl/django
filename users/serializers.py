from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','nombre','apellido','correo','created_at')
        read_only_fields = ('created_at',)
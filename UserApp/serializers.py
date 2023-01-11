from rest_framework import serializers
from .models import CustomerUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = ('id', 'first_name', 'last_name', 'address', 'email', 'phone_number', 'username')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        email = validated_data.get('email', None)
        phone_number = validated_data.get('phone_number', None)
        if email and CustomerUser.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'A user with this email already exists.'})
        if phone_number and CustomerUser.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError({'phone_number': 'A user with this phone number already exists.'})
        user = CustomerUser.objects.create_user(**validated_data)
        return user

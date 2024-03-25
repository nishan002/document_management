from rest_framework import serializers
from account.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type' : 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'confirm_password']
        extra_kwargs = {
            'password' : {'write_only' : True}
        }

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError("Password and Confirm Password didn't matched.")
        return data
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

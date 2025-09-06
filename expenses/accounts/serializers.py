from rest_framework import serializers 
from accounts.models import CustomUser 
from django.contrib.auth.password_validation import validate_password 


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True,required = True,validators = [validate_password])
    password2 = serializers.CharField(write_only = True, required = True)

    class Meta:
        model = CustomUser 
        fields = ('email','password','password2','first_name','last_name','address_line_1','address_line_2')

    
    def validate(self,attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password":"Password Must Match."})
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')
        user = CustomUser.objects.create_user(**validated_data)
        return user
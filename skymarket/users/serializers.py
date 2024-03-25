from django.contrib.auth.hashers import check_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from users.models import User


class UserDefaultSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.get('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserSetPasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField()
    new_password = serializers.CharField()


    def save(self, **kwargs):
        old_password = self.validated_data.get('current_password')
        new_password = self.validated_data.get('new_password')
        user = self.context['request'].user

        if check_password(old_password, user.password):
            user.set_password(new_password)
            user.save()
            return {'info': 'Пароль изменился'}
        else:
            raise ValidationError('Старый пароль неверный')








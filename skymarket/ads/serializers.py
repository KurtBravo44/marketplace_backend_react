from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ads.models import Ad, Comment

class AdSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source='author.first_name')
    author_last_name = serializers.CharField(source='author.last_name')
    author_id = serializers.IntegerField(source='author.id')
    phone = serializers.IntegerField(source='author.phone')

    class Meta:
        model = Ad
        fields = ['pk', 'image', 'title', 'price', 'phone', 'description', 'author_first_name', 'author_last_name', 'author_id']


class AdDefaultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ad
        fields = '__all__'

    def create(self, validated_data):
        ad = Ad.objects.create(**validated_data)
        ad.author = self.context['request'].user
        ad.save()
        return ad


class CommentDefaultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        instance_pk = self.context['view'].kwargs['ad_pk']
        instance_com = Ad.objects.get(pk=instance_pk)

        if not 'text' in validated_data:
            raise ValidationError('Введите текст')
        com = Comment.objects.create(**validated_data)
        com.author = self.context['request'].user
        com.ad = instance_com
        com.save()
        return com
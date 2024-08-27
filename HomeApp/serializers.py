from rest_framework import serializers
from .models import Hero, About


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"


class HeroSerializer(serializers.ModelSerializer):
    video_url = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = Hero
        fields = "__all__"

    def get_video_url(self, obj):
        request = self.context.get('request')
        if obj.video:
            video_url = obj.video.url
            return request.build_absolute_uri(video_url)

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)

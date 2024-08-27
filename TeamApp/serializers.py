from rest_framework import serializers
from .models import Team, Social, Info, Page


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = "__all__"


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__"


class SocialSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Social
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)


class TeamSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    info = InfoSerializer(many=True, read_only=True)
    social = SocialSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)

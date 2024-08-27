from rest_framework import serializers
from .models import Information, Gallery


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = "__all__"


class GallerySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Gallery
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)

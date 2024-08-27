from rest_framework import serializers
from .models import Page, Service, Items, FAQ, FAQItem


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    video_url = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = ['id', 'title', 'subtitle', 'text', 'video', 'video_url']

    def get_video_url(self, obj):
        request = self.context.get('request')
        if obj.video:
            video_url = obj.video.url
            return request.build_absolute_uri(video_url)


class FaqItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQItem
        fields = "__all__"


class FaqSerializer(serializers.ModelSerializer):
    faqItems = FaqItemSerializer(many=True, read_only=True)

    class Meta:
        model = FAQ
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Items
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)

from rest_framework import serializers
from .models import Form, Info, Social, Faq, FaqItem, Page


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = "__all__"


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
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


class InfoSerializer(serializers.ModelSerializer):
    social = SocialSerializer(many=True, read_only=True)

    class Meta:
        model = Info
        fields = "__all__"


class FaqItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqItem
        fields = "__all__"


class FaqSerializer(serializers.ModelSerializer):
    item = FaqItemSerializer(many=True, read_only=True)

    class Meta:
        model = Faq
        fields = "__all__"

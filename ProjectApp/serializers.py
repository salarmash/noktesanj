from rest_framework import serializers
from .models import Category, Project, Gallery, Item, Additional, Page


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
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


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class AddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Additional
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    item = ItemSerializer(many=True, read_only=True)
    gallery = GallerySerializer(many=True, read_only=True)
    addtional = AddSerializer()

    class Meta:
        model = Project
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)

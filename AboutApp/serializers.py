from rest_framework import serializers
from .models import About, Counter, Gallery, Award, AwardItem, History, HistoryItem, Partner, PartnerItem, Page


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = "__all__"


class CounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counter
        fields = "__all__"


class AboutSerializer(serializers.ModelSerializer):
    counter = CounterSerializer(many=True, read_only=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = About
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)


class GallerySerializer(serializers.ModelSerializer):
    image1 = serializers.SerializerMethodField()
    image2 = serializers.SerializerMethodField()

    class Meta:
        model = Gallery
        fields = "__all__"

    def get_image1(self, obj):
        request = self.context.get('request')
        if obj.image1:
            image_url = obj.image1.url
            return request.build_absolute_uri(image_url)

    def get_image2(self, obj):
        request = self.context.get('request')
        if obj.image2:
            image_url = obj.image2.url
            return request.build_absolute_uri(image_url)


class AwardItemSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = AwardItem
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)


class AwardSerializer(serializers.ModelSerializer):
    awardItem = AwardItemSerializer(many=True, read_only=True)

    class Meta:
        model = Award
        fields = "__all__"


class HistoryItemSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = HistoryItem
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)


class HistorySerializer(serializers.ModelSerializer):
    historyItems = HistoryItemSerializer(many=True, read_only=True)

    class Meta:
        model = History
        fields = "__all__"


class PartnerItemSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = PartnerItem
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)


class PartnerSerializer(serializers.ModelSerializer):
    partnerItems = PartnerItemSerializer(many=True, read_only=True)

    class Meta:
        model = History
        fields = "__all__"

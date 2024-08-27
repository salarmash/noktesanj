from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Page, Service, Items, FAQ
from .serializers import PageSerializer, ServiceSerializer, ItemSerializer, FaqSerializer


class ServiceView(APIView):
    def get(self, request):
        service = Service.objects.all().last()
        page = Page.objects.all().last()
        data = {'service': ServiceSerializer(instance=service, context={'request': request}).data,
                'pageDesc': PageSerializer(instance=page).data}
        return Response(data=data, status=status.HTTP_200_OK)


class ItemView(APIView):
    def get(self, request):
        items = Items.objects.all().order_by("-id")[:3]
        data = ItemSerializer(instance=items, many=True, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)


class SingleItem(APIView):
    def get(self, request, pk):
        item = Items.objects.get(id=pk)
        faq = FAQ.objects.get(item=item)
        data = {'item': ItemSerializer(instance=item, context={'request': request}).data,
                'faq': FaqSerializer(instance=faq).data}
        return Response(data=data, status=status.HTTP_200_OK)

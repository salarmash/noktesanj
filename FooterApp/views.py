from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Information, Gallery
from .serializers import InfoSerializer, GallerySerializer


class FooterView(APIView):
    def get(self, request):
        info = Information.objects.all().last()
        gallery = Gallery.objects.all()[:6]
        data = {'info': InfoSerializer(instance=info).data,
                'gallery': GallerySerializer(instance=gallery, many=True, context={'request': request}).data}

        return Response(data=data, status=status.HTTP_200_OK)

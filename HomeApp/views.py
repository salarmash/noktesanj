from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Hero, About
from .serializers import HeroSerializer, AboutSerializer


class HomeView(APIView):
    def get(self, request):
        hero = Hero.objects.all().last()
        about = About.objects.all().last()

        data = {'hero': HeroSerializer(instance=hero, context={'request': request}).data,
                'about': AboutSerializer(instance=about).data}

        return Response(data=data, status=status.HTTP_200_OK)

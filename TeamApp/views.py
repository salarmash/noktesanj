from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Page, Team
from .serializers import PageSerializer, TeamSerializer


class TeamView(APIView):
    def get(self, request):
        team = Team.objects.all()
        page = Page.objects.all().last()
        data = {'team': TeamSerializer(instance=team, many=True, context={'request': request}).data,
                'pageDesc': PageSerializer(instance=page).data}

        return Response(data=data, status=status.HTTP_200_OK)


class SingleView(APIView):
    def get(self, request, pk):
        team = Team.objects.get(id=pk)
        data = TeamSerializer(instance=team, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)

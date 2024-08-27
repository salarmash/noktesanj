from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Page, Category, Project
from .serializers import PageSerializer, CategorySerializer, ProjectSerializer


class ProjectView(APIView):
    def get(self, request):
        project = Project.objects.all()
        page = Page.objects.all().last()
        data = {'project': ProjectSerializer(instance=project, many=True, context={'request': request}).data,
                'pageDesc': PageSerializer(instance=page).data}

        return Response(data=data, status=status.HTTP_200_OK)


class SingleView(APIView):
    def get(self, request, pk):
        project = Project.objects.get(id=pk)
        data = ProjectSerializer(instance=project, context={'request': request}).data

        return Response(data=data, status=status.HTTP_200_OK)


class AllCategoryView(APIView):
    def get(self, request):
        category = Category.objects.all()
        data = CategorySerializer(instance=category, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)


class SingleCategoryView(APIView):
    def get(self, request, pk):
        category = Category.objects.get(id=pk)
        post = Project.objects.filter(category=category)

        data = {'posts': ProjectSerializer(post, many=True, context={'request': request}).data,
                'category': CategorySerializer(instance=category).data}

        return Response(data=data, status=status.HTTP_200_OK)

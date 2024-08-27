from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Category, Author, Post, Page
from .serializers import CategorySerializer, AuthorSerializer, PostSerializer, PageSerializer
from rest_framework.pagination import PageNumberPagination


class AllPostView(APIView):
    def get(self, request):
        articles = Post.objects.all()
        paginator = PageNumberPagination()
        post = paginator.paginate_queryset(queryset=articles, request=request)
        page = Page.objects.all().last()
        data = {'posts': PostSerializer(post, many=True, context={'request': request}).data, 'total': articles.count(),
                'next': paginator.get_next_link(), 'previous': paginator.get_previous_link(),
                'count_per_page': len(post), 'page': PageSerializer(instance=page).data}
        return Response(data=data, status=status.HTTP_200_OK)


class SinglePost(APIView):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        data = PostSerializer(post, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)


class AllCategoryView(APIView):
    def get(self, request):
        category = Category.objects.all()
        data = CategorySerializer(instance=category, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)


class SingleCategoryView(APIView):
    def get(self, request, pk):
        category = Category.objects.get(id=pk)
        post = Post.objects.filter(categories=category)

        data = {'posts': PostSerializer(post, many=True, context={'request': request}).data,
                'category': CategorySerializer(instance=category).data}

        return Response(data=data, status=status.HTTP_200_OK)


class AllAuthorView(APIView):
    def get(self, request):
        author = Author.objects.all()
        data = AuthorSerializer(author, many=True, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)


class SingleAuthorView(APIView):
    def get(self, request, pk):
        author = Author.objects.get(id=pk)
        post = Post.objects.filter(author=author)
        data = {'posts': PostSerializer(instance=post, many=True, context={'request': request}).data,
                'author': AuthorSerializer(instance=author, context={'request': request}).data}
        return Response(data=data, status=status.HTTP_200_OK)

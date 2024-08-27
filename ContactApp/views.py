from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Form, Info, Faq, Page
from ContactApp.serializers import FormSerializer, FaqSerializer, InfoSerializer, PageSerializer


class ContactView(APIView):
    def get(self, request):
        info = Info.objects.all().last()
        faq = Faq.objects.all().last()
        page = Page.objects.all().last()
        data = {'info': InfoSerializer(instance=info, context={'request': request}).data,
                'faq': FaqSerializer(instance=faq).data, 'PageDesc': PageSerializer(instance=page).data}
        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = FormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": 200,
                "message": "درخواست با موفقیت ثبت شذ",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            "status": 400,
            "message": "مشکلی پیش آمده",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

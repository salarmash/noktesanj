from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import About, Gallery, Award, History, Partner,Page
from .serializers import AboutSerializer, GallerySerializer, AwardSerializer, HistorySerializer, PartnerSerializer,PageSerializer


class AboutView(APIView):
    def get(self, request):
        about = About.objects.all().last()
        gallery = Gallery.objects.all().last()
        award = Award.objects.all().last()
        history = History.objects.all().last()
        partner = Partner.objects.all().last()
        page = Page.objects.all().last()

        data = {'about': AboutSerializer(instance=about, context={"request": request}).data,
                'gallery': GallerySerializer(instance=gallery, context={"request": request}).data,
                'award': AwardSerializer(instance=award, context={"request": request}).data,
                'history': HistorySerializer(instance=history, context={"request": request}).data,
                'pageDesc': PageSerializer(instance=page).data,
                'partners': PartnerSerializer(instance=partner, context={"request": request}).data}

        return Response(data=data, status=status.HTTP_200_OK)

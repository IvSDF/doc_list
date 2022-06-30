from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import Doctor, Direction
from .serializers import DoctorSerializer, DirectionSerializer, DocItemSerializer
from .service import DoctorPagination, DoctorFilter


class DirectionAPIView(generics.ListAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer


class DoctorAPIView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = DoctorPagination
    filterset_class = DoctorFilter
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['years_of_experience', 'birthday']


class DocItemAPIView(generics.ListAPIView):

    def get(self, request, slug):
        doc_item = Doctor.objects.get(slug=slug)
        serializer = DocItemSerializer(doc_item)
        return Response(serializer.data)

from django.shortcuts import render
from rest_framework.response import Response

from .serializers import CategoryGoodsSerializers, GoodSerializers
from .models import Category, Goods
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
# Create your views here.


class ListCreateCategoryAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryGoodsSerializers


# class RetrieveUpdateDestroyCategoryAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategoryGoodsSerializers


class RetrieveCategoryAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryGoodsSerializers


class UpdateCategoryAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryGoodsSerializers


class DeleteCategoryAPIView(DestroyAPIView):
    queryset = Category.objects.all()


#Boogs viewlari

class ListCreateGoodsAPIView(ListCreateAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodSerializers


# class RetrieveUpdateDestroyGoodsAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Goods.objects.all()
#     serializer_class = GoodSerializers


class RetrieveGoodsAPIView(RetrieveAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodSerializers


class UpdateGoodsAPIView(UpdateAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodSerializers


class DeleteGoodsAPIView(DestroyAPIView):
    queryset = Goods.objects.all()

















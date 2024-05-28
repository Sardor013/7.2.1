from django.urls import path
from .views import (
    ListCreateCategoryAPIView,
    RetrieveCategoryAPIView,
    UpdateCategoryAPIView,
    DeleteCategoryAPIView,
    # RetrieveUpdateDestroyCategoryAPIView,
    # RetrieveUpdateDestroyGoodsAPIView,
    ListCreateGoodsAPIView,
    RetrieveGoodsAPIView,
    UpdateGoodsAPIView,
    DeleteGoodsAPIView
)

urlpatterns = [
    path('categories/', ListCreateCategoryAPIView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', RetrieveCategoryAPIView.as_view(), name='category-retrieve'),
    path('categories/<int:pk>/update/', UpdateCategoryAPIView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', DeleteCategoryAPIView.as_view(), name='category-delete'),
    # path('categories/<int:pk>/', RetrieveUpdateDestroyCategoryAPIView.as_view(), name='category-detail'),
    # path('goods/<int:pk>/', RetrieveUpdateDestroyGoodsAPIView.as_view(), name='goods-detail'),
    path('goods/', ListCreateGoodsAPIView.as_view(), name='goods-list-create'),
    path('goods/<int:pk>/', RetrieveGoodsAPIView.as_view(), name='goods-retrieve'),
    path('goods/<int:pk>/update/', UpdateGoodsAPIView.as_view(), name='goods-update'),
    path('goods/<int:pk>/delete/', DeleteGoodsAPIView.as_view(), name='goods-delete'),
]
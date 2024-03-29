from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .apps import SalesConfig
from .views import AdViewSet, CommentViewSet, AdMyListAPIView
from rest_framework_nested.routers import NestedDefaultRouter

app_name = SalesConfig.name

ad_router = DefaultRouter()
ad_router.register(r'ads', AdViewSet, basename='Объявление')

com_router = NestedDefaultRouter(ad_router, r'ads', lookup='ad')
com_router.register(r'comments', CommentViewSet, basename='Комментарий')

urlpatterns = [
    path('ads/me/', AdMyListAPIView.as_view(), name='Мои объявления')
] + ad_router.urls + com_router.urls

from django.urls import path
from .views import RedocTemplateView, redoc_json

urlpatterns = [
    path("", RedocTemplateView.as_view(), name="redoc"),
    path("json/", redoc_json)
]
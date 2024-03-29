from django.shortcuts import render
from django.views.generic import TemplateView


class RedocTemplateView(TemplateView):
    template_name = "redoc/redoc.html"


def redoc_json(request):
    return render(request, 'redoc/redoc-2.json')

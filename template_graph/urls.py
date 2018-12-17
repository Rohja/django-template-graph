from django.conf import settings
from django.conf.urls import patterns,  url

from .views import TemplateGraphView


urlpatterns = []

if settings.DEBUG:
    urlpatterns += [
        url(r'^', TemplateGraphView.as_view()),
    ]

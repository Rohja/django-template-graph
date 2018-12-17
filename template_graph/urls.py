from django.conf import settings
from django.conf.urls import url

from .views import TemplateGraphView


urlpatterns = []

if settings.DEBUG:
    urlpatterns += [
        url(r'^', TemplateGraphView.as_view()),
    ]

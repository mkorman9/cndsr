from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from app_interface import views

urlpatterns = [
    url(r'.*', views.root)
]

urlpatterns = format_suffix_patterns(urlpatterns)

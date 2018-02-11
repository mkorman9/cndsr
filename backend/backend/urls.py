from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from backend_interface import views

urlpatterns = [
    path('shorten', views.shorten),
    path('<str:key>', views.go_to)
]

urlpatterns = format_suffix_patterns(urlpatterns)

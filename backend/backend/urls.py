from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from backend import views
from backend.exceptions import handle_not_found

urlpatterns = format_suffix_patterns([
    path('s/shorten', views.shorten),
    path('s/<str:key>', views.go_to),
    url(r'.*', handle_not_found)
])

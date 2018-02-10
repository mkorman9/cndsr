from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from app_interface import views

urlpatterns = [
    path('/', views.hello_world),
    path('add/<int:x>/<int:y>', views.add)
]

urlpatterns = format_suffix_patterns(urlpatterns)

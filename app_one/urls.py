from django.urls import path
from app_one.views import index, catalog, news


urlpatterns = [
    path('', index),
    path('catalog/', catalog),
    path('news/', news)
]

from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.reviews, name="reviews"),
      # re_path(r'^api/reviews/$', views.reviews, name="reviews"),
]
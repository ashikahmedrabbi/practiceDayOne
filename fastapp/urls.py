from django.urls import path, include  # Added include import
from . import views  # Added import for views

urlpatterns = [

    path('app/', views.home),
]

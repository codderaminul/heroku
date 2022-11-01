from django.urls import path,include
from myapp import views
import myapp

urlpatterns = [
    path('', views.index_page),
]

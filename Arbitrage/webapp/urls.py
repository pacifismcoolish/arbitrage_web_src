from django.urls import path
from . import views

urlpatterns = [
    path('<msg>/', views.index, name='index'),
]
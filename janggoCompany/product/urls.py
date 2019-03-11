from django.urls import path
from . import views

urlpatterns = [
    # go to main site
    path('', views.main, name='product'),
    path('<int:pk>/', views.detail, name='product_detail'),
]
from django.urls import path
from . import views
urlpatterns = [
    # go to main site
    path('', views.main, name='home'),
    path('newProduct/', views.model_form_upload, name='new_product'),
    path('en/', views.transEn, name='en'),
    path('ko/', views.transKo, name='ko'),
]

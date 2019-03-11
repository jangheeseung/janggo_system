from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # go to mainsite app's urls
    path('', views.hire_list, name="hire_list"),
    path('create/<int:pk>', views.apply_create, name="apply_create"),
    path('update/', views.apply_update, name="apply_update"),
    path('check/', views.check_apply, name="check_apply"),
    path('hire/', views.hire_create, name="hire_create"),
    path('hire/view/<int:pk>', views.hire_view, name="hire_view"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

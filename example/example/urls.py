from django.urls import path, include
from django.contrib import admin
from .views import index

urlpatterns = [
    path('radmin/', admin.site.urls),
    path('contact/', include('recontact.urls')),
    path('', index)
]


from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', include(('First_App.urls','first_app'),namespace='first_app')),
]


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('serv/', include('serv.urls')),
    path('edu/', include('edu.urls')),

]

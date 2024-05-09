
from django.contrib import admin
from django.urls import path, include
from gestion_ville import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('gestion_ville/', include('gestion_ville.urls')),
   # path('payments/', include('payments.urls')),
]

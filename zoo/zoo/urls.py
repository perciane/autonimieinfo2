from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('animalerie/', include('animalerie.urls')),
    path('admin/', admin.site.urls),
]


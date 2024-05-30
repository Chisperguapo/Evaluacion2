
from django.contrib import admin
from django.urls import path
from quiz import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.datos),
]

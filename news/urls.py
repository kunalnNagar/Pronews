"""
URL configuration for news project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('india/', views.india, name="india"),
    path('world/', views.world, name="world"),
    path('bollywood/', views.bollywood, name="bollywood"),
    path('sports/', views.sports, name="sports"),
    path('search/', views.search, name="search"),
    path('all/', views.all, name="all"),
    path('details/<int:id>/', views.details, name="details"),
    path('accounts/', include("user.urls")),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

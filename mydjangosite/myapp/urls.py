"""mydjangosite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings  # add this
from django.conf.urls.static import static  # add this

from django.contrib import admin
from django.urls import path, include
from . import views , functions
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path("", views.login, name='login'),
                  path('user_login/', views.user_login, name='user_login'),
                  path("Main_App/", views.Main_App, name="Main_App"),
                  path("Main_App/upload_image/", views.upload_image),
                  path(r'image/upload/', views.upload_image, name='upload_image'),
                  path("Main_App/Predict/", views.upload_image),
                  path(r'image/Predict/', views.Predict, name='Predict'),
              ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


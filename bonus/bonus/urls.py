"""bonus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path

from movies_box_api.views import MovieCollection, MovieMember

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Movies Box API')


urlpatterns = [
    path('', schema_view),
    path('api/movies/', MovieCollection.as_view()),
    path('api/movies/<int:pk>', MovieMember.as_view()),
    path('api/movies/filter', MovieMember.as_view()),
    path('admin/', admin.site.urls),
]

"""dj_bootcamp URL Configuration

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
from django.contrib import admin
from django.urls import path

from products.views import (
    search_view,
    product_detail_view,
    product_detail_view_api,
    product_list_view,
    product_create_request,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('search/', search_view),
    path ('products/create/',product_create_request),
    path ('products/<int:pk>/', product_detail_view),
    path ('products/api/<int:pk>/', product_detail_view_api),
    path ('products/', product_list_view),
]

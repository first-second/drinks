"""drinks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import re_path
from drinks import views
from drinks.views import CustomAuthToken

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^drinks/',views.drink_list),
    re_path(r'^drinks/<int:id>',views.drink_details),
    re_path(r'^api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
]

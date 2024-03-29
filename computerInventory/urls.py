"""
URL configuration for computerInventory project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, re_path, include
from inventoryapp.views import home, computer_entry, computer_list, computer_edit, computer_delete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('computer_entry/', computer_entry, name='computer_entry'),
    path('computer_list/', computer_list, name='computer_list'),
    re_path(r'^computer_list/(?P<id>\d+)/$', computer_edit, name='computer_edit'),
    re_path(r'^computer_list/(?P<id>\d+)/delete/$', computer_delete, name='computer_delete'),
    path('accounts/', include('registration.backends.default.urls')),
]

"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from accounts.views import connection, logout_user, register
from shop import settings
from storage.views import add_to_box, box_user, delete_box, index, product_detail
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('regiter/', register, name="register"),
    path('connection/', connection, name="connection"),
    path('logout/', logout_user, name="logout"),
    path('box/', box_user, name="box-user"),
    path('box/delete', delete_box, name="delete-box"),
    path('product/<str:slug>/', product_detail, name="product"),
    path('product/<str:slug>/add_to_box/', add_to_box, name="add-to-box"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

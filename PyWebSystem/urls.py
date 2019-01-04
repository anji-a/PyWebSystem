"""PyWebSystem URL Configuration

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
from django.conf.urls.static import static
from django.urls import path

from django.conf import settings
from PyWebSystem.Web import views
from PyWebSystem.PyUtil import pw_ui_include
from PyWebSystem.PyUtil import ProcessRequest
from PyWebSystem.PyUtil import pw_memory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login', views.index),
    path('workspace', views.login_app),
    path('logout', views.logout_app),
    path('UI_Include', pw_ui_include.pw_ui_include),
    path('processrequest', ProcessRequest.process_request),
    path('memory_check', pw_memory.memory_check),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

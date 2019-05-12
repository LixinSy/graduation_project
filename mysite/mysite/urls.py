"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path, re_path
from myapp import views
from . import settings
from django.views.static import serve

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout', views.logout, name="logout"),
    url(r'^user/', views.user, name='user'),
    url(r'^setting/', views.setting, name='setting'),
    url(r'^alter_user_data/', views.alter_user_data, name='alter_user_data'),
    url(r'^alter_pwd/', views.alter_pwd, name='alter_pwd'),
    url(r'^issue/', views.issue, name='issue'),

    url(r'^media/(?P<path>.*)', serve, {"document_root":settings.MEDIA_ROOT}),
    #url(r'^media/user_figures/(?P<path>.*)', serve, {'document_root':settings.MEDIA_ROOT+'/user_figures'}),
] #+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

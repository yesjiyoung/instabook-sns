"""instabook URL Configuration

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
import snsapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', snsapp.views.home, name = 'home'),
    path('realhome/', snsapp.views.real, name = 'real'),
    path('signup/', snsapp.views.signup, name = 'signup'),
    path('correct/', snsapp.views.correct, name = 'correct'),
    path('uncorrect/', snsapp.views.uncorrect, name = 'uncorrect'),
    path('unlog/', snsapp.views.unlog, name= 'unlong'),
    path('realhome/<int:sns_id>', snsapp.views.detail, name='detail'),
    path('realhome/create', snsapp.views.create, name = "create"),
    path('realhome/update/<int:sns_id>', snsapp.views.update, name='update'),
    path('realhome/delete/<int:sns_id>', snsapp.views.delete, name='delete'),
    
    
]

"""
URL configuration for web project.

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
from django.urls import path
import main.views as mView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mView.index),
    path('login/', mView.login, name='login'),
    path('home/', mView.home, name='home'),
    path('logout/', mView.logout_session, name='logout'),
    path('messages/', mView.messages, name='messages'),
    path('answer/<int:mess_id>', mView.answer, name='answer')
]

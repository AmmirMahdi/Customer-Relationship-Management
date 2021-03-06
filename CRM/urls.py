"""CRM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


from rest_framework import routers
from Lead.views import ModelViewSet
from Opportunity.views import ModelViewSetOPP

from django.contrib.auth.views import LoginView,LogoutView
from Lead.views import HomePageView

router = routers.DefaultRouter()
router.register('leads',ModelViewSet)
router.register('opps', ModelViewSetOPP)



urlpatterns = [
    path('',HomePageView.as_view(), name='home'),
    path('admin/', admin.site.urls),


    path('leads/',include('Lead.urls', namespace='lead')),
    path('opp/',include('Opportunity.urls', namespace='opp')),
    path('contact/', include('Contact.urls', namespace='contact')),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(), name='logout'),


    path('api/',include(router.urls))



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
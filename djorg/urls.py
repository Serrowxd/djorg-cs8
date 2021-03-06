"""djorg URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from notes.api import NoteViewset, PersonalNoteViewset

# from django.conf.urls import url, include ## this is not needed because of routers.


router = routers.DefaultRouter()
router.register(r"notes", NoteViewset)
router.register(r"personal_notes", PersonalNoteViewset)
# you can continue to add more by just adding `router.register` to the line below and swapping out the imports.

urlpatterns = [
    path("admin/", admin.site.urls),
    path(r"api/", include(router.urls)),
    # url(r"^api-auth/", include("rest_framework.urls")), ## this is overwritten by the above path(r"api/") code.
]

# test

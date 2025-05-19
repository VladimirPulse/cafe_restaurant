from django.contrib import admin
from django.urls import path

from menu_app.views import IndexPageView

urlpatterns = [
    path("menu/", IndexPageView.as_view(), name="home"),
    path("menu/<named_url>/", IndexPageView.as_view(), name="menu_item"),
    path("admin/", admin.site.urls),
]

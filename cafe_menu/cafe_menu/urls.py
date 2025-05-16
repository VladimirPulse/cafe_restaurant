from django.contrib import admin
from django.urls import path

from menu_app.views import IndexPageView

urlpatterns = [
    # path('', views.home, name='home'),  # Главная страница
    path('menu/', IndexPageView.as_view(), name='home'),
    path("admin/", admin.site.urls),
]

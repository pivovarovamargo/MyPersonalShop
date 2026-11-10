from django.contrib import admin
from django.urls import path

admin.site.site_header= 'управление'

admin.site.site_title= 'панель'

admin.site.site_title= 'панель'
urlpatterns = [
    path('admin/', admin.site.urls),
]

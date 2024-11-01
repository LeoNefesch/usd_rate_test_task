# from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('usd_rate/', include('usd_rate.urls')),
    path('', lambda request: redirect('get_current_usd')),
]

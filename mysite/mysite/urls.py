from django.contrib import admin
from django.urls import path
from django.conf.urls import include
# from python_library.test_lib2 import test_func

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('home.urls')),
    path('analysis/', include('analysis.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # aika
    # path('', include('register.urls')),
]
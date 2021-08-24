
from index.views import BookViewSet
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('index.urls')),
    path('auth/', obtain_auth_token)
]

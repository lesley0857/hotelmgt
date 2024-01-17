from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView,
)
from rest_framework import permissions
from django.conf.urls.static import static
from django.conf import settings
from Customeruser.views import *
from roomapp.views import *
from guestpreferenceapp.views import *


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('admin/', admin.site.urls),

    path('api/register_user/', User_create.as_view(), name='user_create'),

    path('api/listroom/', Listroom.as_view(), name='listroom'),

    path('api/createpreference/', PreferenceView.as_view(), name='PreferenceView'), 
    path('api/updatepreference/', PreferenceView.as_view(), name='updatepreference'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


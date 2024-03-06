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
from reservation.views import *
from Payment.views import *
from reservation.admin import ReservationModelAdmin
from checkout.views import *


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('admin/', admin.site.urls),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('preference/', preference_view, name='preference'),
    path('signup/', preference_view, name='signup'),
    path('', home_view, name='home'),




    path('api/registerandupdate_user/', User_create.as_view(), name='user_create'),
    # path('api/listroom/', Listroom.as_view(), name='listroom'),

    path('api/preference/', PreferenceView.as_view(), name='PreferenceView'), 
    path('api/preference/<str:email>/', PreferenceView.as_view(), name='getpreference'), 

    path('api/reserve/<str:email>/', ReservationView.as_view(), name='ReservationView'),
    path('api/reservation/', ReservationView.as_view(), name='ReservationView'),

    path('api/checkout/', CheckoutView.as_view(), name='CheckoutView'),

    path('api/payment/',PaymentView.as_view(), name='PaymentView')

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "Hotel manager"
admin.site.index_title = ""
admin.site.site_title = "Anonymous Hotel Manager"
# admin.site.add_action(ReservationModelAdmin)
from .views import RegisterView,GetTokenView
from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns =[
    path('register/',RegisterView.as_view()),
    path('get-token/',GetTokenView.as_view()),
    #path('users/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
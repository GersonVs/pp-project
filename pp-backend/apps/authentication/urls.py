from django.urls import path
from rest_framework_simplejwt.views import (TokenRefreshView, TokenVerifyView)
from apps.authentication.views import CustomObtainTokenPairView

app_name = 'authentication'

urlpatterns = [
    path('api/token/'         , CustomObtainTokenPairView.as_view()),
    path('api/token/refresh/' , TokenRefreshView.as_view()),
    path("api/token/verify/"  , TokenVerifyView.as_view()),
]

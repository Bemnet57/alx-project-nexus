# from django.urls import path
# from . import views

# urlpatterns = [
#     path("register/", views.RegisterView.as_view(), name="register"),
#     path("profile/", views.UserProfileView.as_view(), name="profile"),
# ]


#ask gemini how to write app level urls.py

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView
from .views import CustomTokenObtainPairView

# urlpatterns = [
#     path('register/', RegisterView.as_view(), name='register'),
#     path('login/', TokenObtainPairView.as_view(), name='login'),
#     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]

# urlpatterns = [
#     path("register/", RegisterView.as_view(), name="register"),  # if you already have one
#     path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
#     path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
# ]

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
]

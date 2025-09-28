"""
URL configuration for job_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

# from django.contrib import admin
# from django.urls import path, re_path, include
# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

# schema_view = get_schema_view(
#     openapi.Info(
#         title="Job Board API",
#         default_version='v1',
#         description="API documentation for the Job Board backend",
#         terms_of_service="https://www.example.com/terms/",
#         contact=openapi.Contact(email="support@example.com"),
#         license=openapi.License(name="MIT License"),
#     ),
#     public=True,
#     permission_classes=[permissions.AllowAny],
# )

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/auth/', include('users.urls')),

#     # Swagger docs
#     re_path(r'^swagger(?P<format>\.json|\.yaml)$',
#             schema_view.without_ui(cache_timeout=0), name='schema-json'),
#     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#     path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
# ]


# from django.contrib import admin
# from django.urls import path, re_path, include
# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
# from users.views import CustomTokenObtainPairView
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

# schema_view = get_schema_view(
#     openapi.Info(
#         title="Job Board API",
#         default_version='v1',
#         description="API documentation for the Job Board backend",
#         terms_of_service="https://www.example.com/terms/",
#         contact=openapi.Contact(email="support@example.com"),
#         license=openapi.License(name="MIT License"),
#     ),
#     public=True,
#     permission_classes=[permissions.AllowAny],
# )

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/auth/', include('users.urls')),   # registration & custom auth

#     # JWT Auth
#     path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

#     # Swagger docs
#     re_path(r'^swagger(?P<format>\.json|\.yaml)$',
#             schema_view.without_ui(cache_timeout=0), name='schema-json'),
#     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#     path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
# ]

from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from users.views import CustomTokenObtainPairView, RegisterView
from rest_framework_simplejwt.views import TokenRefreshView

# Swagger/OpenAPI setup
schema_view = get_schema_view(
    openapi.Info(
        title="Job Board API",
        default_version='v1',
        description="API documentation for the Job Board backend",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # User registration
    path('api/register/', RegisterView.as_view(), name='register'),

    # JWT authentication
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Job posts
    path('api/', include('jobs.urls')),

    #Applications
    path('applications/', include('applications.urls')),

    # Swagger/OpenAPI docs
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

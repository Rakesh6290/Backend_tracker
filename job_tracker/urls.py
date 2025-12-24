from django.contrib import admin
from django.urls import path, include
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Smart Job Application Tracker API",
        default_version='v1',
        description="Track job applications with guest login",
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/jobs/', include('jobs.urls')),
    path('swagger/', schema_view.with_ui('swagger')),
]

from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger schema view
schema_view = get_schema_view(
   openapi.Info(
      title="KPRO Task Management",
      default_version='v1',
      description="API documentation for managing projects, developers, tasks, and comments",
      terms_of_service="https://www.google.com/policies/terms/",
      
   ),
   public=True,
)

# from drf_spectacular.views import (
#     SpectacularAPIView,
#     SpectacularRedocView,
#     SpectacularSwaggerView,
# )

urlpatterns = [
    # # API schema generation
    # path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # # Swagger UI
    # path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    # # Redoc UI
    # path("redocs/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    # Include other app URLs (e.g., API endpoints)
    path('admin/', admin.site.urls),
    path('api/', include('task.urls')),  # Include the app URLs
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
]

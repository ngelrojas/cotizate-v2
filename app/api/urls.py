"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

# schema_view = get_schema_view(
#     openapi.Info(
#         title="COTIZATE API V2",
#         default_version="V2",
#         description="cotizate v2 updated new modules",
#         terms_of_service="https://ngelrojasp.com/policies/terms/",
#         contact=openapi.Contact(email="me@ngelrojasp.com"),
#         license=openapi.License(name="BSD License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )
urlpatterns = [
    # re_path(
    #     r"^api/v2/cotizate(?P<format>\.json|\.yaml)$",
    #     schema_view.without_ui(cache_timeout=0),
    #     name="schema-json",
    # ),
    # re_path(
    #     r"^api/v2/cotizate/$",
    #     schema_view.with_ui("swagger", cache_timeout=0),
    #     name="schema-swagger-ui",
    # ),
    # re_path(
    #     r"^api/v2/cotizate/$",
    #     schema_view.with_ui("redoc", cache_timeout=0),
    #     name="schema-redoc",
    # ),
    path("admin/", admin.site.urls),
    path("api/v2/", include("users.urls")),
    path("api/v2/", include("profiles.urls")),
    path("api/v2/", include("profileAssociations.urls")),
    path("api/v2/", include("profileCompanies.urls")),
    path("api/v2/", include("categories.urls")),
    path("api/v2/", include("tags.urls")),
    path("api/v2/", include("campaings.urls")),
    path("api/v2/", include("payments.urls")),
    path("api/v2/", include("comments.urls")),
    path("api/v2/", include("rewards.urls")),
    path("api/v2/", include("favorites.urls")),
    path("api/v2/", include("likes.urls")),
    path("api/v2/", include("countries.urls")),
    path("api/v2/", include("cities.urls")),
    path("api/v2/", include("socialNetworks.urls")),
    path("api/v2/", include("phases.urls")),
    path("api/v2/", include("improvies.urls")),
    path("api/v2/", include("bookmarks.urls")),
    path("api/v2/", include("uploads.urls")),
    path("api/v2/", include("updatings.urls")),
    path("api/v2/", include("denounces.urls")),
    path("api/v2/", include("followers.urls")),
    path("api/v2/", include("contacts.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# use this part in production using gunicorn
urlpatterns += staticfiles_urlpatterns()

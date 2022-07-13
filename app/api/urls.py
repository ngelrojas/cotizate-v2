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
    path("api/v1/", include("users.urls")),
    path("api/v1/", include("profiles.urls")),
    path("api/v1/", include("profileCompanies.urls")),
    path("api/v1/", include("categories.urls")),
    # path("api/v1/", include("tags.urls")),
    path("api/v1/", include("campaings.urls")),
    # path("api/v1/", include("payments.urls")),
    # path("api/v1/", include("comments.urls")),
    path("api/v1/", include("rewards.urls")),
    # path("api/v1/", include("favorites.urls")),
    path("api/v1/", include("likes.urls")),
    path("api/v1/", include("countries.urls")),
    path("api/v1/", include("cities.urls")),
    # path("api/v1/", include("socialNetworks.urls")),
    path("api/v1/", include("phases.urls")),
    # path("api/v1/", include("improvies.urls")),
    path("api/v1/", include("bookmarks.urls")),
    # path("api/v1/", include("uploads.urls")),
    # path("api/v1/", include("updatings.urls")),
    # path("api/v1/", include("denounces.urls")),
    # path("api/v1/", include("followers.urls")),
    # path("api/v1/", include("contacts.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# use this part in production using gunicorn
urlpatterns += staticfiles_urlpatterns()

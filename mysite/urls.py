import debug_toolbar
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("pages.urls")),
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
    path("__debug__/", include(debug_toolbar.urls, namespace="djdt")),
]

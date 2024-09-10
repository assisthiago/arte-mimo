from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import app.core.views

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("", app.core.views.index, name="index"),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + debug_toolbar_urls()
)

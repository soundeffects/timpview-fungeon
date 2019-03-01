from django.conf import settings

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("", include("pinax.blog.urls", namespace="pinax_blog")),
    path("ajax/images/", include("pinax.images.urls", namespace="pinax_images")),
    path("admin/", admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

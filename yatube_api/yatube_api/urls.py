from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from yatube_api.yatube_api.views import PostViewSet

router_posts =  router_groups = routers.DefaultRouter()
router_posts.register('api/v1/posts', PostViewSet)
router_groups.register('api/v1/groups', PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/api-token-auth/', include(router.urls)),
    path('api/v1/posts/', include(router.urls)),
    path('api/v1/posts/<post_id>/', include(router.urls)),
    path('api/v1/groups/', include(router.urls)),
    path('api/v1/groups/<group_id>/', include(router.urls)),
    path('api/v1/posts/<post_id>/comments/', include(router.urls)),
    path('api/v1/posts/<post_id>/comments/<comment_id>/', include(router.urls)),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )

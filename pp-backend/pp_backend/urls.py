from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from reviews.views import ProductViewSet, ImageViewSet
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'product', ProductViewSet, basename='Product')
# router.register(r'image', ImageViewSet, basename='Image')

urlpatterns = [
    path('admin/'         , admin.site.urls),
    path('authentication/', include('apps.authentication.urls', namespace='authentication')),
    path('core/'          , include('apps.core.urls'          , namespace='core')),
    # path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
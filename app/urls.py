from django.urls import path, include

from .views import BlogView, CommentView, LikeViewSet

urlpatterns = [

]



from django.urls import path, include
from .views import FoodView, TypeView, CommentView, CompositionView

from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)


from rest_framework import routers


router = routers.SimpleRouter()
router.register('blog', BlogView)
router.register('comment', CommentView)
router.register('like', LikeViewSet)


urlpatterns = [
    path('', include(router.urls)),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),


]
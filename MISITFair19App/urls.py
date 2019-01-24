from rest_framework import routers
from .views import PiImageSave
from .models import District

from django.conf.urls import url, include

router = routers.DefaultRouter()
#router.register(r'ImageExtractAPI', ImageViewSet) , BaseAPICallURL ,BaseUrlConfig
#router.register(r'registration', Registration)


router.register(r'savenewpiimage', PiImageSave)

# Wire up our API with our urls
urlpatterns = [
    url(r'^', include(router.urls)),
]
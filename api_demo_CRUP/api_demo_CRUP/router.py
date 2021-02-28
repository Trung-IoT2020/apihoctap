from api.viewsets import APIsViewsets
from rest_framework import routers

router=routers.DefaultRouter()
router.register('',APIsViewsets)
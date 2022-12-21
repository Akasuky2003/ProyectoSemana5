from . import api
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'pagos', api.TodoViewSetCustom, 'pagosCustom')

api_urlpatterns = router.urls
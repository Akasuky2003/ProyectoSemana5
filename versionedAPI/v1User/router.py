from . import api
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'User', api.TodoViewSetCustom, 'UserCustom')

api_urlpatterns = router.urls
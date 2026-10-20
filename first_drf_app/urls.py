from rest_framework.routers import DefaultRouter
from .views import NumberViewSets

router = DefaultRouter()
router.register('numbers', NumberViewSets)

urlpatterns = router.get_urls()
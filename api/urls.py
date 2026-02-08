from rest_framework.routers import DefaultRouter
from .views import PeliculaViewSet, DirectorViewSet

router = DefaultRouter()
router.register(r'peliculas', PeliculaViewSet)
router.register(r'directores', DirectorViewSet)   # ✅ nuevo

urlpatterns = router.urls
from rest_framework.routers import DefaultRouter
from .views import IngredientViewSet, RecipeViewSet

router = DefaultRouter()
router.register('ingredients', IngredientViewSet, basename='ingredients')
router.register('recipes', RecipeViewSet, basename='recipes')

urlpatterns = router.urls
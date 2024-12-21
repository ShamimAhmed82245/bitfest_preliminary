from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Ingredient, Recipe
from .serializers import IngredientSerializer, RecipeSerializer
import pytesseract
from PIL import Image

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    @action(detail=False, methods=['post'])
    def parse_recipe_image(self, request):
        image = request.FILES.get('image')
        if not image:
            return Response({'error': 'No image provided'}, status=status.HTTP_400_BAD_REQUEST)

        text = pytesseract.image_to_string(Image.open(image))
        return Response({'parsed_text': text}, status=status.HTTP_200_OK)

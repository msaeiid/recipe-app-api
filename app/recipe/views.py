"""View for Recipe APIs.
"""

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Recipe
from recipe import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    """View for manage recipe APIs."""
    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_query_set(self):
        """Retrieve recipes for authenticate user."""
        # because of IsAuthenticate we know that user is authenticated
        return self.queryset.filter(user=self.request.user).order_by('-id')

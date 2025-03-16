from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint for viewing and editing items
    """
    queryset = Item.objects.all().order_by('-created_at')
    serializer_class = ItemSerializer
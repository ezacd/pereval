from django.forms import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

from .models import Pereval
from .serializers import *


class PerevalViewSet(ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer


@api_view(['POST'])
def submit_data(request):
    serializer = PerevalSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)


@api_view(['GET'])
def get_data(pk):
    try:
        perevals = Pereval.objects.get(pk=pk)
    except Exception:
        return Response(status=404)

    serializer = PerevalSerializer(perevals)
    return Response(serializer.data)

# {
#     "beauty_title": "1",
#     "title": "1",
#     "other_titles": "1",
#     "connect": "1",
#     "coordinates": 1,
#     "user_added": 1,
#     "level": 1
# }

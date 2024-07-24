from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from profiller.models import Profil
from profiller.api.serializers import ProfilSerializer

class ProfilList(generics.ListCreateAPIView):
    queryset = Profil.objects.all()
    serializer_class = ProfilSerializer
    permission_classes = [IsAdminUser]
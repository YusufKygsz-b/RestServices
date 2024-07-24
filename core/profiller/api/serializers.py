from profiller.models import Profil, ProfilState
from rest_framework import serializers

class ProfilSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only = True)
    photo = serializers.ImageField(read_only=True)

    class Meta:
        model = Profil
        fields = '__all__'


class ProfileFotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profil
        field = ['photo']


class ProfileStateSerializer(serializers.ModelSerializer):
    user_profil = serializers.StringRelatedField(read_only = True)

    class Meta:
        model = ProfilState
        field = '__all__'
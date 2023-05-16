from rest_framework import serializers
from .models import Guest, Movie,Reservation

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

class ReservationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"

class GuestSerializers(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['pk','reservations','name','mobile']
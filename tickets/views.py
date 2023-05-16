from django.http import JsonResponse
from django.shortcuts import render
from tickets.models import Guest,Movie,Reservation
from .serializers import GuestSerializers, MovieSerializer,ReservationSerializers
from rest_framework.decorators import api_view
from rest_framework import status, filters
from rest_framework.response import Response

# Create your views here.

#Without REST and no model query FBV 

def no_rest_no_model(request):
    guests = [
        {
            'id':1, 'name': 'mohamed','mobile':3443
        },
        {
            'id':2, 'name': 'Morsi','mobile':453
        },

    ]
    return JsonResponse(guests,safe= False)

#Without REST and using model:

def no_rest_form_model(request):
    guest_data = Guest.objects.all()
    movie_data = Movie.objects.all()
    response = {
        'guests': list(guest_data.values('name','mobile')),
        'movie':list(movie_data.values('Movie'))
    }
    return JsonResponse(response)

# List == GET
# Create == POST
# pk query == GET 
# Update == PUT
# Delete destroy == DELETE

#3 Function based views 
#3.1 GET POST
@api_view(['GET','POST'])
def FBV_List(request):
    # GET
    if request.method == 'GET':
        guests = Guest.objects.all()
        serializer = GuestSerializers(guests, many=True)
        return Response(serializer.data)
    # POST
    elif request.method == 'POST':
        serializer = GuestSerializers(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
    

# 3.2 GET PUT DELETE
@api_view(['GET','PUT','DELETE'])
def FBk_List(request,pk):
    guest = Guest.objects.get(pk = pk)
    # GET
    if request.method == 'GET':
        serializer = GuestSerializers(guest)
        return Response(serializer.data)
    # POST
    elif request.method == 'PUT':
        serializer = GuestSerializers(guest, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
            guest.delete()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
    
from django.http import Http404, JsonResponse
from django.shortcuts import render
from tickets.models import Guest,Movie,Reservation
from .serializers import GuestSerializers, MovieSerializer,ReservationSerializers
from rest_framework.decorators import api_view
from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins, viewsets


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
    
        # DELETE

    elif request.method == 'DELETE':
            guest.delete()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
    

# 4.1 GET and POST from rest framework Class Based View APIView
class CBV_List(APIView):
    def get(self,request):
        guests = Guest.objects.all()
        serializer = GuestSerializers(guests,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = GuestSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status= status.HTTP_201_CREATED)
        else:
            return Response(
                status= status.HTTP_400_BAD_REQUEST
            )
                
# 4.2 GET, PUT, DELETE from rest framework Class Based View APIView

class CBV_List_PK(APIView):
    def get_object(self,pk):
        try:
            return Guest.objects.get(pk=pk)
        except Guest.DoesNotExist:
            raise Http404
    
    def get(self,request,pk):
        guest = self.get_object(pk)
        serializer = GuestSerializers(guest)
        return Response(serializer.data)
    
    def put(self,request,pk):
        guest = self.get_object(pk)
        serializer = GuestSerializers(guest,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        guest = self.get_object(pk)
        guest.delete()
        return Response(status.HTTP_204_NO_CONTENT)
    

# 5.1 GET, POST from rest framework Class Based View mixins:

class Mixins(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializers
    
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
    

# 5.1 GET, POST from rest framework Class Based View mixins:

class Mixins_PK(mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializers

    def get(self,request,pk):
        return self.retrieve(request)
    def put(self,request,pk):
        return self.update(request)
    def delete(self,request,pk):
        return self.destroy(request)


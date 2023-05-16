from django.urls import path
from . import views
urlpatterns = [

    #1
    path('no_rest_no_model/',views.no_rest_no_model,name = 'no_rest_no_model'),

    #2
    path('no_rest_form_model/',views.no_rest_form_model,name = 'no_rest_form_model'),

    #3: GET and POST from rest framework, and functions based views
    path('rest/',views.FBV_List,name = 'FBV_List'),

    #4: GET ,PUT and DELETE from rest framework, and functions based views
    path('rest/<int:pk>/',views.FBk_List,name = 'FBV_List'),




]

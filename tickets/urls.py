from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('guests',viewsets_guest)
# router.register('movies',viewsets_movie)
# router.register('reservations',viewsets_reservation)


urlpatterns = [
    # 1 Without REST and No model query FBV - CBV
    path("no_rest_no_model/", views.no_rest_no_model, name="no_rest_no_model"),
    # 2 Without REST and Using model:
    path("no_rest_form_model/", views.no_rest_form_model, name="no_rest_form_model"),


    # 3.1: GET and POST from rest framework, and functions based views
    path("rest/FBV", views.FBV_List, name="FBV_List"),
    # 3.2: GET ,PUT and DELETE from rest framework, and functions based views
    path("rest/<int:pk>/", views.FBk_List, name="FBk_List"),

    # 4.1 GET and POST from rest framework, and Class based views
    path("rest/CBV", views.CBV_List.as_view(), name="CBV_List"),
    # 4.2: GET and POST from rest framework, and Class based views
    path("rest/CBV/<int:pk>/", views.CBV_List_PK.as_view(), name="CBV_List_PK"),


    # 5.1 GET and POST from rest framework, and Class based views Mixins
    path("rest/mixins", views.Mixins.as_view(), name="Mixins"),

    # 5.2 GET and POST from rest framework, and Class based views Mixins_pk
    path("rest/mixins/<int:pk>/", views.Mixins_PK.as_view(), name="Mixins_PK"),


    # 5.2 GET and POST from rest framework, and Class based views Mixins_pk
    path("rest/generic/", views.Generics.as_view(), name="Generics"),


    # 5.2 GET and POST from rest framework, and Class based views Mixins_pk
    path("rest/Generics_PK/<int:pk>", views.Generics_PK.as_view(), name="Generics_PK"),

    # #7 Viewsets
    # path('rest/viewsets/', include(router.urls)),

    # 8 find movie:
    path('fbv/findmovie', views.find_movie),
    path('fbv/new_reservation', views.new_reservation),

    
    
    ]

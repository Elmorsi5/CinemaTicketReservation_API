from django.urls import path
from . import views

urlpatterns = [
    # 1 Without REST and No model query FBV - CBV
    path("no_rest_no_model/", views.no_rest_no_model, name="no_rest_no_model"),
    # 2 Without REST and Using model:
    path("no_rest_form_model/", views.no_rest_form_model, name="no_rest_form_model"),


    # 3.1: GET and POST from rest framework, and functions based views
    path("rest/", views.FBV_List, name="FBV_List"),
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


]

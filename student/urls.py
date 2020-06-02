from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('form with default arg/', views.showFormData,name="register"),
    path('form with fields arg/', views.formFieldwithAguments,name="form_fields_arg"),
]
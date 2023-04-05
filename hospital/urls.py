from django.urls import path
from .views import *

urlpatterns = [
    path('', patient_list, name='patient_list'),
    path('search/', search, name='search'),

    path('create/', create_patient, name='create_patient'),
    path('update/<int:pk>/', update_patient, name='update_patient'),
    path('delete/<int:pk>/', delete_patient, name='delete_patient'),
]
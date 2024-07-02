from django.urls import path
from .views import signup, login_view, patient_dashboard, doctor_dashboard, logout_view
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('patient_dashboard/', patient_dashboard, name='patient_dashboard'),
    path('doctor_dashboard/', doctor_dashboard, name='doctor_dashboard'),
    path('logout/', logout_view, name='logout'),
    
]

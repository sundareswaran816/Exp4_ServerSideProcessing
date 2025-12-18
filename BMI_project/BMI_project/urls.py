from django.contrib import admin
from django.urls import path
from BMI_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('bmi', views.bmi_calculator, name='bmi'),
]
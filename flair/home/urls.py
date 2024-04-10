from django.urls import path
from .views import home, calculate_readability

urlpatterns = [
    path('', home, name='home'),
    path('calculate-readability/', calculate_readability, name='calculate_readability'),
]

app_name = "home"
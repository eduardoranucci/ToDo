from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.SignUp.as_view(), name='sign_up'),
]

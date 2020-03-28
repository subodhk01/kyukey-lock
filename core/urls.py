from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index" ),
    path('generate_otp', views.generate_otp),
    path('remove_otp/<otp_id>', views.remove_otp),

    # Auth Views
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name="logout"),
]
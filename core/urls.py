from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index" ),
    path('generate_otp', views.generate_otp),
    path('generate_otp/success/<id>', views.generation_success, name="generation_success"),
    path('hide_otp', views.hide_otp),
    path('remove_otp/<otp_id>', views.remove_otp),
    path('lock_history', views.lock_history),

    # Auth Views
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name="logout"),

    # API Views
    path('otp_validation/<otp>', views.opt_validation)
]
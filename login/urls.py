from django.urls import path
from . import views

urlpatterns =[
    path("login",views.login_session,name="login"),
    path("signup",views.signup,name="signup"),
    path("logout",views.logout_session,name="logout"),
]
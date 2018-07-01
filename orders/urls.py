from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/register", views.register, name="register"),
    path("/login", views.loginn, name="login"),
    path("/logout", views.logoutt, name="logout"),
    path("/makeorder", views.makeorder, name="makeorder"),
    path("/confirmorder", views.confirmorder, name="confirmorder"),
    path("/confirmedorder", views.confirmedorder, name="confirmedorder"),
    
]

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = "App"

urlpatterns = [
    path("", views.login, name="login"),
    path("login", views.login, name="login"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("create-appointment", views.create_appointment, name="create-appointment"),
    path("today-appointment", views.today_appointment, name="today-appointment"),
    path("all-appointment", views.all_appointment, name="all-appointment"),
    path("register", views.register, name="register"),

]

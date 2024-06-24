
from django.urls import path
from . import views
urlpatterns = [
    path('signup/',views.UserRegistrationView.as_view()),
    path('login/',views.LoginView.as_view())
]

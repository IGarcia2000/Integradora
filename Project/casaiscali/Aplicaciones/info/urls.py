from django.urls import path
from .views import SignUpView


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("respass/", SignUpView.as_view(), name="respass")
]
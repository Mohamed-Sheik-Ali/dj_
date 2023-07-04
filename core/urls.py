from django.urls import path
from .views import UserSignupApiview

urlpatterns = [
  path("signup/", UserSignupApiview.as_view()),
]

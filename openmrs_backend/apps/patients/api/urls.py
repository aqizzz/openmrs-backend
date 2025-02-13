from django.urls import path
from . import views

urlpatterns = [
  path('user/<int:id>', views.user_detail),
  path('user/create', views.user_create),
  path('user/login', views.SankofiaTokenObtainPairView.as_view()),
]

from django.urls import path
from . import views

urlpatterns = [
  path('users/<int:id>', views.user_detail),
  path('user/create', views.user_create),
  path('user/token/', views.SankofiaTokenObtainPairView.as_view()),
]

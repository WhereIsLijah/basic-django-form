from django.urls import path
from accesspoint import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('home/', views.homepage, name='home'),
]

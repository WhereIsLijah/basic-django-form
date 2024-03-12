# Import the views module
from django.urls import path
from . import views  # Add this import statement

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # URL pattern for rendering the signup form
    path('signup/', views.signup, name='signup'),

    # URL pattern for processing signup form submissions
    # You can use the same view for form submission processing
    path('signup/submit/', views.signup, name='signup_submit'),

    # URL pattern for rendering the login form
    path('login/', views.login_view, name='login'),

    # URL pattern for processing login form submissions
    # You can use the same view for form submission processing
    path('login/submit/', views.login_view, name='login_submit'),
]

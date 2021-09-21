from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views 


urlpatterns = [
    path('signup/', views.signup, name='signup'),

    # path("password_reset/", views.password_reset_request, name="password_reset"),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
    #     template_name="admin/accounts/password/password_reset_confirm.html"), name='password_reset_confirm'),
]
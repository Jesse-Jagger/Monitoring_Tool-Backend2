from django.urls import path
from users.views import RegisterView, LoginView, LogoutView, UserProfileView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"), # Public Access-AllowAny
    path("login/", LoginView.as_view(), name="login"), # Public Access-AllowAny
    path("logout/", LogoutView.as_view(), name="logout"), # Authenticated
    path("profile/", UserProfileView.as_view(), name="profile"), # Authenticated
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"), # Authenticated
]

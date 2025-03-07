from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from users.views import (
    RegisterView,
    LoginView,
    LogoutView,
    UserProfileView,
    UserManagementView,
    ServerManagementView,
    RealTimeServerStatusView,
    ServerLogsView,
    AlertsView,
    ReportsView,
    AdminDashboardView,
    SystemSettingsView,
    APIAccessView,
    CodebaseAccessView,
)

urlpatterns = [
    # Authentication
    path("register/", RegisterView.as_view(), name="register"),  # Admin & Devs Only
    path("login/", LoginView.as_view(), name="login"),  # Public
    path("logout/", LogoutView.as_view(), name="logout"),  # Authenticated Only
    path("profile/", UserProfileView.as_view(), name="profile"),  # Authenticated Only
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),  # Refresh Token

    # Role-Based Access Views
    path("users/manage/", UserManagementView.as_view(), name="user_management"),  # Admin Only
    path("servers/manage/", ServerManagementView.as_view(), name="server_management"),  # Admin, IT, Developer
    path("servers/status/", RealTimeServerStatusView.as_view(), name="real_time_status"),  # Admin, IT, Developer
    path("servers/logs/", ServerLogsView.as_view(), name="server_logs"),  # Admin, IT, Developer, Customer Engagement
    path("alerts/", AlertsView.as_view(), name="alerts"),  # Admin, IT, Developer, Customer Engagement
    path("reports/", ReportsView.as_view(), name="reports"),  # Admin, IT, Developer, Customer Engagement, Flexipay
    path("admin/dashboard/", AdminDashboardView.as_view(), name="admin_dashboard"),  # Admin Only
    path("settings/", SystemSettingsView.as_view(), name="system_settings"),  # Admin Only
    path("api/access/", APIAccessView.as_view(), name="api_access"),  # Admin, IT, Developer
    path("codebase/", CodebaseAccessView.as_view(), name="codebase_access"),  # Admin, IT, Developer, Ebanking Support
]
